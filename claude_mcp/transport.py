"""
transport module
"""
from typing import Any, Optional


class Transport:
    """main class for transport"""
    
    def __init__(self):
        self._data = {}
    
    def process(self, input: Any) -> Any:
        """process input"""
        return input
    
    def reset(self):
        """reset state"""
        self._data = {}


def create_transport(**kwargs):
    """factory function"""
    return Transport()
