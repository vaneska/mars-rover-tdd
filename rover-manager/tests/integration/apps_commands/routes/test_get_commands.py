from domains.shared.entities import Command, CommandList
from infra.gateways import redis
from infra.rover.repositories import CommandListRedisRepo
from werkzeug.test import TestResponse


def test_success(client):
    r = redis.get_instance()
    r.delete(CommandListRedisRepo.KEY_NAME)
    command_list_repo = CommandListRedisRepo()
    command_list_repo.push_commands(
        command_list=CommandList(commands=[Command.MOVE, Command.LEFT])
    )
    command_list_repo.push_commands(
        command_list=CommandList(commands=[Command.RIGHT, Command.MOVE])
    )

    response: TestResponse = client.get("/commands")

    assert response.json == {"commands": ["ML", "RM"]}
