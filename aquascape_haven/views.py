from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from checkout.models import Order
from community.models import Community

@login_required
def account_dashboard(request):
    """
    View to display the user's details, order history and community posts.
    """
    orders = Order.objects.filter(email=request.user.email).order_by('-date')
    posts = Community.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'account/dashboard.html', {
        'user': request.user,
        'orders': orders,
        'posts': posts,
    })