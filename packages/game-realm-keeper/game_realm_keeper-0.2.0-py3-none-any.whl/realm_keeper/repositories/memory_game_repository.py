# memory_game_repository.py
from typing import Dict, Optional
from realm_keeper.models.game_repository import GameRepository
from realm_keeper.models.game_world import GameWorld

class MemoryGameRepository(GameRepository):
    def __init__(self):
        self.games: Dict[str, GameWorld] = {}

    def save_game_state(self, game_id: str, game_world: GameWorld) -> None:
        self.games[game_id] = game_world

    def load_game_state(self, game_id: str) -> Optional[GameWorld]:
        return self.games.get(game_id)

    def delete_game_state(self, game_id: str) -> None:
        if game_id in self.games:
            del self.games[game_id]
