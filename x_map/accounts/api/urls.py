from django.urls import path
from accounts.api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'auth'

urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('check-login/', views.check_login_api_handler, name='check_login'),
  path('register/', views.register_api_handler, name='register'), 
]