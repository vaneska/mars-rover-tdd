import logging
import time

from domains.rover.entities import Rover
from domains.rover.use_cases import ProcessCommandsUseCase
from infra.rover.repositories import (
    CommandListRedisRepo,
    RoverPositionRedisRepo,
)
from infra.rover.transmitters import MarsRoverHTTPTransmitter

logging.basicConfig(level=logging.INFO)


def process_commands():
    position_repo = RoverPositionRedisRepo()
    use_case = ProcessCommandsUseCase(
        rover_transmitter=MarsRoverHTTPTransmitter(
            rover=Rover(position=position_repo.load_position())
        ),
        position_repo=position_repo,
        commands_list_repo=CommandListRedisRepo(),
        logger=logging.getLogger(),
    )
    use_case.execute()


def run():
    while True:
        process_commands()
        time.sleep(1)


if __name__ == "__main__":
    run()
