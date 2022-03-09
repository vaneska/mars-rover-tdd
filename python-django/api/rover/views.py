from enum import Enum

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from dataclasses import asdict,dataclass
import json


class DirectionType(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"


@dataclass
class Point:
    x: int
    y: int
    direction: DirectionType


class Rover:
    def __init__(self, point: Point = Point(0, 0, DirectionType.North)) -> None:
        self.current_point = point

    def move(self) -> Point:
        if self.current_point.direction == DirectionType.North:
            self.current_point.y += 1

        elif self.current_point.direction == DirectionType.East:
            self.current_point.x += 1

        elif self.current_point.direction == DirectionType.South:
            self.current_point.y -= 1

        elif self.current_point.direction == DirectionType.West:
            self.current_point.x -= 1

        return self.current_point

    def rotate_left(self) -> Point:
        pass

    def rotate_right(self) -> Point:
        pass


class Commands(APIView):

    @csrf_exempt
    def coffee(self):
        return HttpResponse("I'm a teapot", status=status.HTTP_418_IM_A_TEAPOT)

    @csrf_exempt
    def post(self, request: HttpRequest):
        commands_str = json.loads(request.body).get("command")
        array_of_commands = list(commands_str)
        rover = Rover()
        for command in array_of_commands:
            if command == "M": point = rover.move()
            elif command == "L": point = rover.rotate_left()
            elif command == "R": point = rover.rotate_right()

        return JsonResponse({"point": asdict(point)}, status=status.HTTP_201_CREATED)
