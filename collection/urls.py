from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

app_name = 'collection'
urlpatterns = [
    path('console/<int:pk>/', views.ConsoleDetailView.as_view(), name="console-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)