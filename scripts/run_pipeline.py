import logging
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from src.adapters.SourceX import SourceXAdapter
from src.config.loader import load_sources_config, ConfigLoadError
from src.llm.pure_python_agent import PurePythonFilterAgent
from src.storage.db import SessionLocal, engine
from src.storage.models import RawVacancy, FilteredVacancy, Base

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

logging.info(f"CWD: {os.getcwd()}")
logging.info(f"__file__: {__file__}")

def main():
    # 1. Initialization
    try:
        sources = load_sources_config(Path(__file__).parent.parent / "config" / "sources.yaml")
    except ConfigLoadError as e:
        logging.critical(f"Pipeline aborted: {e}")
        sys.exit(1)
    Base.metadata.create_all(engine)
    sources_dict = sources.sources
    adapter = SourceXAdapter(sources_dict["SourceX"])
    llm = PurePythonFilterAgent()

    # 2. Fetch & Normalize
    raw = adapter.fetch_raw()
    normalized = [adapter.normalize(r) for r in raw]
    logger.info(f"Fetched {len(normalized)} items")

    # 3. Idempotent Upsert Raw
    with SessionLocal() as sess:
        for item in normalized:
            sess.merge(RawVacancy(**item))
        sess.commit()

    # 4. LLM Filter & Save
    results = []
    for item in normalized:
        llm_res = llm.evaluate(item)
        results.append({
            "id": item["id"], "source_id": item["id"],
            "llm_pass": llm_res["pass"], "confidence": llm_res["confidence"],
            "reason": llm_res["reason"], "tags": json.dumps(llm_res["tags"]),
            "processed_at": datetime.now(timezone.utc)
        })
    with SessionLocal() as sess:
        for r in results:
            sess.merge(FilteredVacancy(**r))
        sess.commit()
    logger.info(f"Processed: {len(results)}. Passed: {sum(1 for r in results if r['llm_pass'])}")

if __name__ == "__main__":
    main()
