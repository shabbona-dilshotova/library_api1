from django.shortcuts import render
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializers, UserSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet


class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializers(books, many=True)
    return Response(serializer.data)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookUpdateApi(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializers(isinstance=book, data=data, partial=True)
        if serializer.is_valid(ralse_exception=True):
            book_saved = serializer.save()
            return Response(
                data={
                    'status': True,
                    'message': f'book {book_saved} update successsfully'
                }
            )


from django.contrib.auth import get_user_model


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
