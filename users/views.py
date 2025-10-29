from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def account_view(request):
    return render(request, 'users/account.html', {'user': request.user})
