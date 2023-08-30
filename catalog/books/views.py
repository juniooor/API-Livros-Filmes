from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookSerializer
from .models import Book
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.
