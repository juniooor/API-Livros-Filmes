# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from books.serializers import BookSerializer
from books.models import Book


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    


