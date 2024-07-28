# game_world.py
from typing import Dict, Any, List, Optional
from .game_object import GameObject

class GameWorld:
    def __init__(self):
        self.objects: Dict[str, GameObject] = {}
        self.rules: List[str] = []

    def add_object(self, obj: GameObject):
        self.objects[obj.id] = obj

    def get_object(self, object_id: str) -> Optional[GameObject]:
        return self.objects.get(object_id)

    def update_object(self, obj: GameObject):
        if obj.id in self.objects:
            self.objects[obj.id] = obj

    def remove_object(self, object_id: str):
        self.objects.pop(object_id, None)

    def add_rule(self, rule: str):
        self.rules.append(rule)

    def get_rules(self) -> List[str]:
        return self.rules.copy()

    def get_state(self) -> Dict[str, Any]:
        return {
            "objects": {id: obj.model_dump() for id, obj in self.objects.items()},
            "rules": self.rules
        }
