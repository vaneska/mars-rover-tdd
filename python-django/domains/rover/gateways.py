from abc import ABC, abstractmethod

from domains.rover.entities import Command, Position


class RoverGatewayException(Exception):
    pass


class RoverLowPowerException(RoverGatewayException):
    pass


class RoverIsBusyException(RoverGatewayException):
    pass


class RoverUnknownException(RoverGatewayException):
    pass


class RoverGateway(ABC):
    @abstractmethod
    def process_command(self, command: Command) -> Position:
        pass
