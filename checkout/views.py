import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from marketplace.models import Product
from django.shortcuts import render

def checkout(request):
    return render(request, 'checkout/checkout.html')

stripe.api_key = settings.STRIPE_SECRET_KEY


