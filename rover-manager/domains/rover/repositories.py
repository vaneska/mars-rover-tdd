from abc import ABC, abstractmethod

from domains.shared.entities import CommandList, Position

class NoCommandsException(Exception):
    pass

class RoverPositionRepo(ABC):
    @abstractmethod
    def load_position(self) -> Position:
        pass

    @abstractmethod
    def save_position(self, position: Position) -> bool:
        pass


class CommandListRepo(ABC):
    @abstractmethod
    def pop_commands(self) -> CommandList:
        pass

    @abstractmethod
    def push_commands(self, command_list: CommandList) -> bool:
        pass
