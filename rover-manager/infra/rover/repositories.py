import json
from typing import List

from attrs import define
from domains.rover.repositories import (
    CommandListRepo,
    NoCommandsException,
    RoverPositionRepo,
)
from domains.shared.entities import CommandList, DirectionType, Position
from infra.gateways import redis
from redis import Redis


@define
class RoverPositionFakeRepo(RoverPositionRepo):
    position: Position

    def load_position(self) -> Position:
        return self.position

    def save_position(self, position: Position) -> bool:
        self.position = position
        return True


class RoverPositionRedisRepo(RoverPositionRepo):

    KEY_NAME = "rover:position"

    def __init__(self) -> None:
        self._redis: Redis = redis.get_instance()

    def load_position(self) -> Position:
        position_json = self._redis.get(self.KEY_NAME)

        if position_json is None:
            return Position(x=0, y=0, direction=DirectionType.North)

        position_json = json.loads(position_json)
        return Position(
            x=position_json["x"],
            y=position_json["y"],
            direction=DirectionType(position_json["direction"]),
        )

    def save_position(self, position: Position) -> bool:
        result = self._redis.set(self.KEY_NAME, json.dumps(position.dict()))
        return bool(result)


class CommandListFakeRepo(CommandListRepo):
    _commands: List[str]

    def __init__(self) -> None:
        self._commands = []

    def pop_commands(self) -> CommandList:

        return CommandList.validate(commands_str=self._commands.pop(0))

    def push_commands(self, command_list: CommandList) -> bool:
        self._commands.append(str(command_list))
        return True

    def fetch_list(self) -> List[CommandList]:
        return [CommandList.validate(c) for c in self._commands]


class CommandListRedisRepo(CommandListRepo):
    KEY_NAME = "rover:commands"

    def __init__(self) -> None:
        self._redis: Redis = redis.get_instance()

    def pop_commands(self) -> CommandList:
        commands_str = self._redis.lpop(self.KEY_NAME)
        if not commands_str:
            raise NoCommandsException()
        return CommandList.validate(commands_str=commands_str.decode("utf-8"))

    def push_commands(self, command_list: CommandList) -> bool:
        self._redis.rpush(self.KEY_NAME, str(command_list))
        return True

    def fetch_list(self) -> List[CommandList]:
        return [
            CommandList.validate(c.decode("utf-8"))
            for c in self._redis.lrange(self.KEY_NAME, 0, -1)
        ]
