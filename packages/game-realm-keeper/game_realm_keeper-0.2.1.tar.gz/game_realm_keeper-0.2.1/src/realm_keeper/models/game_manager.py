from typing import Any, Dict
from uuid import uuid4
from .game_repository import GameRepository
from .game_world import GameWorld
from .game_object import GameObject

class GameManager:
    def __init__(self, game_id: str, repository: GameRepository):
        self.game_id = game_id
        self.repository = repository
        self.game_world = self.repository.load_game_state(game_id) or GameWorld()

    def save_state(self):
        self.repository.save_game_state(self.game_id, self.game_world)

    def create_character(self, name: str) -> str:
        char_id = str(uuid4())
        character = GameObject(id=char_id, type="character", attributes={"name": name})
        self.game_world.add_object(character)
        self.save_state()
        return f"Created character '{name}' with ID {char_id}"

    def create_item(self, name: str) -> str:
        item_id = str(uuid4())
        item = GameObject(id=item_id, type="item", attributes={"name": name})
        self.game_world.add_object(item)
        self.save_state()
        return f"Created item '{name}' with ID {item_id}"

    def set_attribute(self, object_id: str, attribute: str, value: Any) -> str:
        obj = self.game_world.get_object(object_id)
        if obj:
            obj.attributes[attribute] = value
            self.game_world.update_object(obj)
            self.save_state()
            return f"Set {attribute} to {value} for object {object_id}"
        return f"Object {object_id} not found"

    def equip_item(self, character_id: str, item_id: str, slot: str) -> str:
        character = self.game_world.get_object(character_id)
        item = self.game_world.get_object(item_id)
        if character and item:
            if character.type != "character":
                return f"Object {character_id} is not a character"
            if item.type != "item":
                return f"Object {item_id} is not an item"
            character.equipment[slot] = item
            self.game_world.update_object(character)
            self.save_state()
            return f"Equipped {item.attributes['name']} to {character.attributes['name']} in slot {slot}"
        return "Character or item not found"

    def get_game_state(self) -> Dict[str, Any]:
        return self.game_world.get_state()

    def get_formatted_game_state(self) -> str:
        state = self.game_world.get_state()
        formatted_state = "Current game state:\n"
        for obj_id, obj in state["objects"].items():
            formatted_state += f"- {obj['attributes'].get('name', 'Unnamed')} ({obj['type']}):\n"
            for attr, value in obj['attributes'].items():
                if attr != 'name':
                    formatted_state += f"  {attr}: {value}\n"
            if 'equipment' in obj and obj['equipment']:
                formatted_state += "  Equipment:\n"
                for slot, item in obj['equipment'].items():
                    formatted_state += f"    {slot}: {item['attributes'].get('name', 'Unnamed')}\n"
                    for attr, value in item['attributes'].items():
                        if attr != 'name':
                            formatted_state += f"      {attr}: {value}\n"
        return formatted_state

    def add_rule(self, rule: str) -> str:
        self.game_world.add_rule(rule)
        return f"Added rule: {rule}"

    def get_rules(self) -> str:
        rules = self.game_world.get_rules()
        if rules:
            return "Game Rules:\n" + "\n".join(f"- {rule}" for rule in rules)
        return "No rules defined yet."

    def remove_object(self, object_id: str) -> str:
        obj = self.game_world.get_object(object_id)
        if obj:
            self.game_world.remove_object(object_id)
            return f"Removed object {obj.attributes.get('name', 'Unnamed')} with ID {object_id}"
        return f"Object {object_id} not found"

    def list_objects(self, object_type: str = None) -> str:
        objects = self.game_world.get_state()["objects"]
        filtered_objects = objects if object_type is None else {k: v for k, v in objects.items() if
                                                                v['type'] == object_type}

        if not filtered_objects:
            return f"No objects found{' of type ' + object_type if object_type else ''}."

        result = f"{'All objects' if object_type is None else object_type.capitalize() + 's'}:\n"
        for obj_id, obj in filtered_objects.items():
            result += f"- {obj['attributes'].get('name', 'Unnamed')} (ID: {obj_id})\n"
        return result
