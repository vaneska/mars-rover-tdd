from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from dataclasses import asdict,dataclass
import json

@dataclass
class Point:
    x: int
    y: int
    direction: str

class RoverGateway:
    def move(self) -> Point:
        return Point(x = 2, y = 3, direction = "N")

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
        commands_str = json.loads(request.body).get("data")
        array_of_commands = list(commands_str)
        gw = RoverGateway()
        for command in array_of_commands:
            if command == "M": point = gw.move()
            elif command == "L": point = gw.rotate_left()
            elif command == "R": point = gw.rotate_right()

        return JsonResponse({"point": asdict(point)}, status=status.HTTP_201_CREATED)
