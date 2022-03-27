from turtle import position

from celery import Celery
from domains.rover.entities import Rover
from domains.rover.use_cases import ProcessCommandsUseCase
from domains.shared.entities import CommandList
from infra.rover.transmitters import MarsRoverHTTPTransmitter
from infra.rover.repositories import RoverPositionRedisRepo
from pydantic import BaseSettings, Field, RedisDsn


class CelerySettings(BaseSettings):
    REDIS_DSN: RedisDsn = Field(
        default="redis://mars-redis:6379/2", env="REDIS_DSN_FOR_CELERY"
    )


app = Celery("tasks", broker=CelerySettings().REDIS_DSN)


@app.task
def process_commands(commands: str):
    position_repo = RoverPositionRedisRepo()
    use_case = ProcessCommandsUseCase(
        rover_transmitter=MarsRoverHTTPTransmitter(
            rover=Rover(position=position_repo.get_current_position())
        ),
        position_repo=position_repo,
    )
    use_case.execute(command_list=CommandList.validate(commands_str=commands))
