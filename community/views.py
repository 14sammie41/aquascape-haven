from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Community
from .forms import CommunityForm


def community_feed(request):
    """
    View to show all community posts
    """
    posts = Community.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'posts': posts})


@login_required
def create_post(request):
    """
    View to create a new community post
    """
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created.')
            return redirect('community:post_detail', pk=post.pk)
        else:
            return render(request, 'community/create_post.html', {
                'form': form})
    else:
        form = CommunityForm()
        return render(request, 'community/create_post.html', {'form': form})


@login_required
def post_update(request, pk):
    """
    View to update an existing community post
    """
    post = get_object_or_404(Community, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')
            return redirect('community:post_detail', pk=post.pk)
    else:
        form = CommunityForm(instance=post)
    return render(request, 'community/create_post.html', {
            'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    """
    View to delete a community post
    """
    post = get_object_or_404(Community, pk=pk, user=request.user)
    post.delete()
    messages.warning(request, 'Post deleted.')
    return redirect('community:community')

def post_detail(request, pk):
    """
    View to show a single community post
    """
    post = get_object_or_404(Community, pk=pk)
    return render(request, 'community/post_detail.html', {'post': post})
