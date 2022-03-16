from attr import validate
from celery import Celery
from domains.rover.entities import CommandList
from domains.rover.use_cases import ProcessCommandsUseCase
from infra.rover.gateways import MarsRoverHTTPGateway
from infra.rover.repositories import RoverPositionRedisRepo

app = Celery()


@app.task
def process_commands(commands):
    use_case = ProcessCommandsUseCase(
        rover_gateway=MarsRoverHTTPGateway(),
        position_repo=RoverPositionRedisRepo(),
    )
    use_case.execute(command_list=CommandList.validate(commands_str=commands))
