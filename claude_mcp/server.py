"""
server module
"""
from typing import Dict, Any, List
import json


class Server:
    """base server"""
    
    def __init__(self, name: str):
        self.name = name
        self.handlers: Dict[str, callable] = {}
    
    def register(self, method: str, handler: callable):
        """register a handler"""
        self.handlers[method] = handler
    
    def handle(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """handle a request"""
        method = request.get("method")
        params = request.get("params", {})
        
        if method not in self.handlers:
            return {"error": f"unknown method: {method}"}
        
        try:
            result = self.handlers[method](params)
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
