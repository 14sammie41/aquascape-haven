from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Community
from .forms import CommunityForm

def community_feed(request):
    posts = Community.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('community:community')
        else:
            return render(request, 'community/create_post.html', {'form': form})
    else:
        form = CommunityForm()
        return render(request, 'community/create_post.html', {'form': form})
