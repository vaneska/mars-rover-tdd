import http

import pytest
import responses
from domains.rover.entities import Command, DirectionType, Position, Rover
from domains.rover.managers import (
    RoverIsBusyException,
    RoverLowPowerException,
    RoverUnknownException,
)
from infra.rover.managers import (
    MarsRoverErrorMessage,
    MarsRoverHTTPManager,
    MarsRoverHTTPSettings,
)


@responses.activate
def test_successful_processed_command():
    settings = MarsRoverHTTPSettings()
    responses.add(
        responses.GET,
        settings.base_url + settings.url_part_move,
        json={"result": "Команда выполнена успешно!"},
        status=http.HTTPStatus.OK,
    )

    manager = MarsRoverHTTPManager(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )

    position = manager.process_command(Command.MOVE)

    assert position == Position(x=0, y=1, direction=DirectionType.North)


@responses.activate
def test_low_power_error():
    settings = MarsRoverHTTPSettings()
    responses.add(
        responses.GET,
        settings.base_url + settings.url_part_move,
        json={"error": MarsRoverErrorMessage.LOW_POWER.value},
        status=http.HTTPStatus.SERVICE_UNAVAILABLE,
    )

    manager = MarsRoverHTTPManager(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )

    with pytest.raises(RoverLowPowerException):
        manager.process_command(Command.MOVE)


@responses.activate
def test_is_busy_error():
    settings = MarsRoverHTTPSettings()
    responses.add(
        responses.GET,
        settings.base_url + settings.url_part_move,
        json={"error": MarsRoverErrorMessage.IS_BUSY.value},
        status=http.HTTPStatus.SERVICE_UNAVAILABLE,
    )

    manager = MarsRoverHTTPManager(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )

    with pytest.raises(RoverIsBusyException):
        manager.process_command(Command.MOVE)


@responses.activate
def test_unknown_error():
    settings = MarsRoverHTTPSettings()
    settings = MarsRoverHTTPSettings()
    responses.add(
        responses.GET,
        settings.base_url + settings.url_part_move,
        json={"error": "test"},
        status=http.HTTPStatus.SERVICE_UNAVAILABLE,
    )

    manager = MarsRoverHTTPManager(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )

    with pytest.raises(RoverUnknownException):
        manager.process_command(Command.MOVE)
