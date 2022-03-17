import zope.event.classhandler
from domains.shared.events import RoverPositionChanged


@zope.event.classhandler.handler(RoverPositionChanged)
def send_position_to_front(event: RoverPositionChanged) -> None:
    pass
