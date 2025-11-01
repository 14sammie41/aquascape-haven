from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('', views.view_basket, name='view_basket'),
]