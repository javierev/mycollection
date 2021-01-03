from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Console
from .serializers import ConsoleSerializer
# Create your views here.

class ConsoleDetailView(APIView):
    """
    API endpoints to get, put and delete consoles.
    """

    def get(self, request, pk, format=None):
        console = get_object_or_404(Console, pk=pk)
        serializer = ConsoleSerializer(console)
        return JsonResponse(serializer.data)