from django.urls import path
from . import views
from .views import gallery_view

urlpatterns = [
    path('', gallery_view, name='gallery'),
]