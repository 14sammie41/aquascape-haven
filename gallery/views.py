from django.shortcuts import render
from .models import Aquascape

def gallery_view(request):
    aquascapes = Aquascape.objects.all().order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'aquascapes': aquascapes})
