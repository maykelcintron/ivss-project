from django.urls import path
from django.urls import include
from .views import AuthenticationUsers

urlpatterns = [
    path('authlogin/', AuthenticationUsers.as_view(), name = 'aplicacion para autenticar usuario')
]
