import json

from domains.shared.entities import DirectionType, Position
from infra.gateways import redis
from infra.shared.repositories import RoverPositionRedisRepo


def test_get_empty_position():
    r = redis.get_instance()
    r.delete(RoverPositionRedisRepo.KEY_NAME)
    result = RoverPositionRedisRepo().get_current_position()

    assert result == Position(x=0, y=0, direction=DirectionType.North)


def test_get_exist_position():
    r = redis.get_instance()
    expected_position = Position(x=5, y=5, direction=DirectionType.South)
    r.set(
        RoverPositionRedisRepo.KEY_NAME, json.dumps(expected_position.dict())
    )

    result = RoverPositionRedisRepo().get_current_position()

    assert result == expected_position
