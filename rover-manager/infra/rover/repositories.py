import json

from attrs import define
from domains.rover.repositories import RoverPositionRepo
from domains.shared.entities import DirectionType, Position
from infra.gateways import redis
from redis import Redis


@define
class RoverPositionFakeRepo(RoverPositionRepo):
    position: Position

    def get_current_position(self) -> Position:
        return self.position

    def set_position(self, position: Position) -> bool:
        self.position = position
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
