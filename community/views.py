from django.shortcuts import render, redirect
from .models import Community
from .forms import CommunityForm

def community_view(request):
    messages = Community.objects.order_by('-created_at')
    form = CommunityForm()
    
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community_post = form.save(commit=False)
            community_post.user = request.user
            community_post.save()
            return redirect('community_view')
        
    return render(request, 'community/community.html', {'messages': messages, 'form': form})
