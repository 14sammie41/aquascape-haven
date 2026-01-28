from django.contrib import admin
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cancel/', views.cancel, name='cancel'),
    path('order/<order_number>/', views.order_detail, name='order_detail'),
    path('wh/', views.stripe_webhook, name='stripe_webhook'),
    path('success/<order_number>/', views.success, name='success'),
]