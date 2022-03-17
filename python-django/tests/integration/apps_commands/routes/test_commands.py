from infra.gateways import redis
from infra.shared.repositories import RoverPositionRedisRepo
from werkzeug.test import TestResponse


def test_success(client):
    r = redis.get_instance()
    r.delete(RoverPositionRedisRepo.KEY_NAME)
    response: TestResponse = client.post("/commands", json={"command": "MRML"})

    assert response.json == {"point": {"x": 1, "y": 1, "direction": "N"}}
