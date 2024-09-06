from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("hello/", views.HelloWorldView.as_view(), name='hello_world' )
    path("create/", views.BookCreateView.as_view())
    # path("books/",)
    # path("books/",)
    # path("books/",)
]
