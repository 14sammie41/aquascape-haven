from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('competition/', include('competition.urls')),
    path('community/', include('community.urls')),
    path('gallery/', include('gallery.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('success/', TemplateView.as_view(template_name='marketplace/success.html'), name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
