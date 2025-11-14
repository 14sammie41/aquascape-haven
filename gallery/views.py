from django.shortcuts import render
from .models import Aquascape


def gallery_view(request):
    """
    View to display all aquascapes in the gallery.
    """
    aquascapes = Aquascape.objects.all().order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'aquascapes': aquascapes})
