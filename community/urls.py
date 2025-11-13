from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_feed, name='community'),
    path('create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.create_post, name='create_post'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
