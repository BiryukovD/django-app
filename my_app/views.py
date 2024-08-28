from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {
            'message': 'Hello, world!',
        }
        return Response(data, status=status.HTTP_200_OK)
