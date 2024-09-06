# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
# from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema

class UserRegistrationView(APIView):
    @extend_schema(
        request=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer},
        summary="Create a new ExampleModel instance",
        description="Create a new instance of ExampleModel with the provided data.",)
   

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
