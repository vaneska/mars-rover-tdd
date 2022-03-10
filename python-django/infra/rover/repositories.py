import json

from domains.rover.entities import DirectionType, Position
from domains.rover.repositories import RoverPositionRepo
from infra.gateways import redis
from redis import Redis


class RoverPositionFakeRepo(RoverPositionRepo):
    def get_current_position(self) -> Position:
        return Position(x=0, y=0, direction=DirectionType.North)

    def set_position(self, position: Position) -> bool:
        return True


class RoverPositionRedisRepo(RoverPositionRepo):

    KEY_NAME = "rover:position"

    def __init__(self) -> None:
        self._redis: Redis = redis.get_instance()

    def get_current_position(self) -> Position:
        position_json = self._redis.get(self.KEY_NAME)

        if position_json is None:
            return Position(x=0, y=0, direction=DirectionType.North)

        position_json = json.loads(position_json)
        return Position(
            x=position_json["x"],
            y=position_json["y"],
            direction=DirectionType(position_json["direction"]),
        )

    def set_position(self, position: Position) -> bool:
        result = self._redis.set(self.KEY_NAME, json.dumps(position.dict()))
        return bool(result)
