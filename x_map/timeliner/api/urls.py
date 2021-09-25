from django.urls import path
from timeliner.api import views

app_name = 'timeliner'

urlpatterns = [
  path('', views.check, name='check')
]