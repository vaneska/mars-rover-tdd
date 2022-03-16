import requests
from attrs import define
from domains.rover.entities import Command, Position, Rover
from domains.rover.gateways import (
    RoverGateway,
    RoverIsBusyException,
    RoverLowPowerException,
    RoverUnknownException,
)
from pydantic import BaseSettings, Field, HttpUrl


@define
class MarsRoverGateway(RoverGateway):
    rover: Rover

    def _move_rover(self, command: Command) -> None:
        if command == Command.MOVE:
            self.rover.move()
        elif command == Command.LEFT:
            self.rover.rotate_left()
        elif command == Command.RIGHT:
            self.rover.rotate_right()

    def _send_command(self, command: Command) -> bool:
        return True

    def process_command(self, command: Command) -> Position:
        if self._send_command(command=command):
            self._move_rover(command=command)
        return self.rover.position


class MarsRoverHTTPSettings(BaseSettings):
    BASE_URL: HttpUrl = Field(
        default="http://rover:3000/", env="MARS_ROVER_BASE_URL"
    )


class MarsRoverHTTPGateway(MarsRoverGateway):
    def _send_command(self, command: Command) -> bool:

        if command == Command.MOVE:
            url_part = "move"
        elif command == Command.LEFT:
            url_part = "left"
        elif command == Command.RIGHT:
            url_part = "right"

        response: requests.Response = requests.get(
            MarsRoverHTTPSettings.BASE_URL + url_part
        )

        if response.status_code != "200":
            self._raise_exception(response.json.get("error", ""))

        return True

    def _raise_exception(self, error_str):

        if error_str == "Низкий заряд батареи":
            raise RoverLowPowerException()
        elif error_str == "Планетоход занят":
            raise RoverIsBusyException()
        else:
            raise RoverUnknownException()
