# game_manager_factory.py
from typing import Dict
from uuid import uuid4
from .game_repository import GameRepository
from .game_manager import GameManager

class GameSessionManager:
    def __init__(self, repository: GameRepository):
        self.repository = repository
        self.active_games: Dict[str, GameManager] = {}

    def create_game(self) -> str:
        game_id = str(uuid4())
        game_manager = GameManager(game_id, self.repository)
        self.active_games[game_id] = game_manager
        game_manager.save_state()
        return game_id

    def get_game_manager(self, game_id: str) -> GameManager:
        if game_id not in self.active_games:
            game_world = self.repository.load_game_state(game_id)
            if game_world:
                self.active_games[game_id] = GameManager(game_id, self.repository)
            else:
                raise ValueError(f"No game found with id {game_id}")
        return self.active_games[game_id]

    def end_game_session(self, game_id: str) -> bool:
        if game_id in self.active_games:
            del self.active_games[game_id]
            return True
        return False

    def delete_game(self, game_id: str) -> bool:
        if game_id in self.active_games:
            del self.active_games[game_id]
        self.repository.delete_game_state(game_id)
        return True
