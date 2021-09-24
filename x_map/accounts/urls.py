from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.login_api_handler, name='login'),
  path('register/', views.register_api_handler, name='register'), 
]