from abc import ABC, abstractmethod

from domains.rover.entities import Position


class RoverPositionRepo(ABC):
    @abstractmethod
    def get_current_position(self) -> Position:
        pass

    @abstractmethod
    def set_position(self, position: Position) -> bool:
        pass
