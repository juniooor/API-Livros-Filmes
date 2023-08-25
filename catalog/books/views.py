# from django.shortcuts import render
from books.models import Book
from rest_framework import viewsets
from rest_framework import permissions
from catalog.books.serializers import BookSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    


