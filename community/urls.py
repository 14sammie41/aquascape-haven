from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.Community, name='community'),
    path('create/', views.create_post, name='create_post'),
]