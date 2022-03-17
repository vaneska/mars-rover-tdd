from turtle import position

from celery import Celery
from domains.rover.entities import CommandList, Rover
from domains.rover.use_cases import ProcessCommandsUseCase
from infra.rover.managers import MarsRoverHTTPManager
from infra.shared.repositories import RoverPositionRedisRepo

app = Celery()


@app.task
def process_commands(commands: str):
    position_repo = RoverPositionRedisRepo()
    use_case = ProcessCommandsUseCase(
        rover_manager=MarsRoverHTTPManager(
            rover=Rover(
                position=position_repo.get_current_position()
            )
        ),
        position_repo=position_repo
    )
    use_case.execute(command_list=CommandList.validate(commands_str=commands))
