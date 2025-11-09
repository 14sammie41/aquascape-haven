from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from marketplace.models import Product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

import stripe

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    basket = request.session.get('basket', {})
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            line_items = []
            order_total = 0
            
            order = form.save(commit=False)
            order.original_basket = basket
            order.save()
            
            for item_id, item_data in basket.items():
                product = get_object_or_404(Product, pk=item_id)
                line_total = product.price * quantity
                order_total += line_total
                
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                
                line_items.append({
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.price * 100),
                    },
                    'quantity': quantity,
                })
            order.total = order_total
            order.save()

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout_success', args=[order.order_number])
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('checkout_home')
                ),
            )
            order.stripe_pid = session.payment_intent
            order.save()
            
            return redirect(session.url, code=303)
        
        return render(request, 'checkout/checkout.html', {'form': form, 'basket': basket})
    
    form = OrderForm()
    return render(request, 'checkout/checkout.html', {'form': form, 'basket': basket})

def checkout_success(request, order_number):
    order_number = request.session.get('order_number')
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'checkout/checkout_success.html', {'order': order})
