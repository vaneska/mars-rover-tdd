import json

from domains.shared.entities import Command, CommandList
from infra.gateways import redis
from infra.rover.repositories import CommandListRedisRepo


def test_push_and_pop_commands():
    r = redis.get_instance()
    r.delete(CommandListRedisRepo.KEY_NAME)
    commands_list = CommandList(commands=[Command.LEFT, Command.MOVE])
    CommandListRedisRepo().push_commands(command_list=commands_list)

    result = CommandListRedisRepo().pop_commands()

    assert result == commands_list
