from .serializers import BookSerializer
from rest_framework import permissions, generics
from .models import Book
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response


# class BookCreateView(generics.CreateAPIView):
#     @extend_schema(
#     request=BookSerializer,
#     responses={201: BookSerializer},
#     summary="Create a new ExampleModel instance",
#     description="Create a new instance of ExampleModel with the provided data.")
    
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    # # Разрешение доступа только для авторизованных пользователей
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.user = self.request.user
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Book registered successfully."}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class BookCreateView(generics.CreateAPIView):
    # @extend_schema(
    # request=BookSerializer,
    # responses={201: BookSerializer},
    # summary="Create a new ExampleModel instance",
    # description="Create a new instance of ExampleModel with the provided data.")

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только для авторизованных пользователей

    def perform_create(self, serializer):
        # Установите текущего пользователя в поле user
        print(serializer)
        print(self.request.user)
        serializer.save(user=self.request.user)     


