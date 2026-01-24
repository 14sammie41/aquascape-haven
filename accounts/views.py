from allauth.account.views import LoginView, SignupView
from django.shortcuts import redirect
from django.contrib import messages

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)
    
class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)