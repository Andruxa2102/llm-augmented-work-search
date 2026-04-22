import time, random, httpx
from typing import List, Dict
from .base import JobSource

class SourceXAdapter(JobSource):
    source_name = "SourceX"
    def __init__(self, cfg: Dict):
        self.cfg = cfg

    def fetch_raw(self) -> List[Dict]:
        time.sleep(random.uniform(self.cfg.get("rate_limit",{}).get("min_delay_s",2),
                                  self.cfg.get("rate_limit",{}).get("max_delay_s",5)))
        # Здесь будет реальный requests.get + bs4 парсинг
        # Для MVP возвращаем эмуляцию:
        return [
            {"title": "Python Developer", "company": "TechCorp", "url": "https://x.com/1", "description": "FastAPI, SQL, Ollama..."},
            {"title": "Junior Manager", "company": "SalesInc", "url": "https://x.com/2", "description": "Звонки, встречи, CRM..."}
        ]
