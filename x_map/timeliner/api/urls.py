from django.urls import path
from timeliner.api import views

app_name = 'timeliner'

urlpatterns = [
  path('', views.fetch_all_timeline_handler, name='fetch_all'),
  path('u/', views.fetch_user_timeline_handler, name='fetch_user_timeline'),
  path('p/<str:pid>', views.fetch_user_timeline_post_handler, name='fetch_user_timeline_post'),
]