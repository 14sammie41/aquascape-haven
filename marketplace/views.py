from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def product_list(request):
    """
    A view to show all products in the marketplace
    """
    products = Product.objects.all()
    return render(request, 'marketplace/marketplace.html', {
        'products': products})


def create_checkout_session(request, product_id):
    """
    A view to create a Stripe checkout session
    """
    product = get_object_or_404(Product, id=product_id)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/marketplace/success/'),
        cancel_url=request.build_absolute_uri('/marketplace/cancel/'),
    )
    return redirect(checkout_session.url, code=303)


def success(request):
    """
    A view to show the success page after payment
    """
    return render(request, 'marketplace/success.html')


def cancel(request):
    """
    A view to show the cancel page after payment
    """
    return render(request, 'marketplace/cancel.html')


def product_view(request, pk):
    """
    A view to show a single product's details
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_view.html', {
        'product': product})
        