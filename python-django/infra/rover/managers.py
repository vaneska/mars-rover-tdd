import http
from enum import Enum

import requests
from attrs import define
from domains.rover.entities import Command, Position, Rover
from domains.rover.managers import (
    RoverIsBusyException,
    RoverLowPowerException,
    RoverManager,
    RoverUnknownException,
)
from pydantic import BaseSettings, Field, HttpUrl


class MarsRoverErrorMessage(Enum):
    LOW_POWER = "Низкий заряд батареи"
    IS_BUSY = "Планетоход занят"


@define
class MarsRoverManager(RoverManager):
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
    base_url: HttpUrl = Field(
        default="http://rover:3000/", env="MARS_ROVER_BASE_URL"
    )
    url_part_move: str = Field(default="move")
    url_part_left: str = Field(default="left")
    url_part_right: str = Field(default="right")


class MarsRoverHTTPManager(MarsRoverManager):
    def _send_command(self, command: Command) -> bool:

        settings = MarsRoverHTTPSettings()

        if command == Command.MOVE:
            url_part = settings.url_part_move
        elif command == Command.LEFT:
            url_part = settings.url_part_left
        elif command == Command.RIGHT:
            url_part = settings.url_part_right

        response: requests.Response = requests.get(
            settings.base_url + url_part
        )

        if response.status_code != http.HTTPStatus.OK:
            self._raise_exception(response.json().get("error", ""))

        return True

    def _raise_exception(self, error_str):

        if error_str == MarsRoverErrorMessage.LOW_POWER.value:
            raise RoverLowPowerException()
        elif error_str == MarsRoverErrorMessage.IS_BUSY.value:
            raise RoverIsBusyException()
        else:
            raise RoverUnknownException()
