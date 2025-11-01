from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create-checkout-session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', TemplateView.as_view(template_name='marketplace/success.html'), name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('product/<int:pk>/', views.product_view, name='product_view'),
]
