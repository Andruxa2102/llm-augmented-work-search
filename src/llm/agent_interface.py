from abc import ABC, abstractmethod
from typing import Dict, Any

class LLMFilterAgent(ABC):
    @abstractmethod
    def evaluate(self, vacancy: Dict[str, Any]) -> Dict[str, Any]: ...
