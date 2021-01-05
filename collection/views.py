from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Console
from .serializers import ConsoleSerializer
from .permissions import IsOwner
# Create your views here.

class ConsoleDetailView(generics.RetrieveAPIView):
    """
    API endpoints to get, put and delete consoles.
    """
    permission_classes = [IsOwner]
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer