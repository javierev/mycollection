from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views
from rest_framework_simplejwt import views as jwt_views

app_name = 'collection'
urlpatterns = [
    path('console/<int:pk>/', views.ConsoleDetailView.as_view(), name="console-detail"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)