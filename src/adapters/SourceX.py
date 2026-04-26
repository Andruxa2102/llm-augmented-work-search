import time, random, httpx
from typing import List, Dict
from .base import JobSource
from ..config.models import SourceConfig


class SourceXAdapter(JobSource):
    source_name = "SourceX"
    def __init__(self, cfg: SourceConfig):
        self.cfg = cfg

    def fetch_raw(self) -> List[Dict]:
        min_delay = self.cfg.rate_limit.min_delay_s
        max_delay = self.cfg.rate_limit.max_delay_s
        time.sleep(random.uniform(min_delay, max_delay))
        # Здесь будет реальный requests.get + bs4 парсинг
        # Для MVP возвращаем эмуляцию:
        return [
            {"title": "Python Developer", "company": "TechCorp", "url": "https://x.com/1", "description": "FastAPI, SQL, Ollama..."},
            {"title": "Junior Manager", "company": "SalesInc", "url": "https://x.com/2", "description": "Звонки, встречи, CRM..."}
        ]
