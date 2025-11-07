import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from marketplace.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from forms import OrderForm
from .models import Order, OrderLineItem

def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.original_basket = request.session.get('basket', {})
            order.stripe_pid = request.POST.get('stripe_pid')
            order.save()
            
            product = Product.objects.first()  # Example: get a product
            line_item = OrderLineItem(
                order=order,
                product=product,
                quantity=1
            )
            line_item.save()
            
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': int(product.price * 100),
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout_success', args=[order.order_number])
                ),
                cancel_url=request.build_absolute_uri(reverse('checkout_cancel')),
            )
            
            order.stripe_pid = session.payment_intent
            order.save()
            
            return redirect(session.url, code=303)
    else:
        form = OrderForm()
        
    return render(request, 'checkout/checkout.html', {'form': form})

def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'checkout/checkout_success.html', {'order': order})

stripe.api_key = settings.STRIPE_SECRET_KEY
