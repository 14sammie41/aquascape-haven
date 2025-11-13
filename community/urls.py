from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_feed, name='community'),
    path('create/', views.create_post, name='create_post'),
]
