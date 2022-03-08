from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView


class Commands(APIView):

    @csrf_exempt
    def coffee(self):
        return HttpResponse("I'm a teapot", status=status.HTTP_418_IM_A_TEAPOT)



