# game_repository.py
from abc import ABC, abstractmethod
from typing import Optional
from .game_world import GameWorld

class GameRepository(ABC):
    @abstractmethod
    def save_game_state(self, game_id: str, game_world: GameWorld) -> None:
        pass

    @abstractmethod
    def load_game_state(self, game_id: str) -> Optional[GameWorld]:
        pass

    @abstractmethod
    def delete_game_state(self, game_id: str) -> None:
        pass
