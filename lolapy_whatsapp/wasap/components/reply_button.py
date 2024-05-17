from abc import ABC
import json


class ReplyButton(ABC):
    def __init__(self, id: str, title: str) -> None:
        self.id = id
        self.title = title
        
    def __str__(self):
        button = {
            "type": "reply",
            "reply": {"id": self.id, "title": self.title }
        }
        return json.dumps(button)
        
    
    def __repr__(self):
        return f"ReplyButton(id={self.id}, title={self.title})"
        
    
    def __eq__(self, other):
        return self.id == other.id and self.title == other.title


