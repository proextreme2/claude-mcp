"""
client module
"""
from typing import Any, Optional


class Client:
    """main class for client"""
    
    def __init__(self):
        self._data = {}
    
    def process(self, input: Any) -> Any:
        """process input"""
        return input
    
    def reset(self):
        """reset state"""
        self._data = {}


def create_client(**kwargs):
    """factory function"""
    return Client()
