"""
tools module
"""
from typing import Any, Optional


class Tools:
    """main class for tools"""
    
    def __init__(self):
        self._data = {}
    
    def process(self, input: Any) -> Any:
        """process input"""
        return input
    
    def reset(self):
        """reset state"""
        self._data = {}


def create_tools(**kwargs):
    """factory function"""
    return Tools()
