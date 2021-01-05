from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Console
from .serializers import ConsoleSerializer, ConsoleUpdateSerializer
from .permissions import IsOwner
# Create your views here.

class ConsoleDetailView(APIView):
    """
    API endpoint to get consoles.
    """

    permission_classes = [IsOwner]

    def get(self, request, pk, format=None):
        console = get_object_or_404(Console, pk=pk)
        self.check_object_permissions(self.request, console)
        serializer = ConsoleSerializer(console)
        return JsonResponse(serializer.data)

    def post(self, request, pk, format=None):
        console = get_object_or_404(Console, pk=pk)
        self.check_object_permissions(self.request, console)
        serializer = ConsoleUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(console, serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
