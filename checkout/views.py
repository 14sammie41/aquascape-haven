from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from marketplace.models import Product
from decimal import Decimal

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def _basket_totals(basket):
    total = Decimal('0.00')
    items = []
    for item_id, qty in basket.items():
        product = get_object_or_404(Product, id=item_id)
        lineitem_total = product.price * qty
        items.append({
            'product': product,
            'quantity': qty,
            'lineitem_total': lineitem_total,
        })
        total += product.price * qty
    return total, items

def checkout(request):
    
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect('view_basket')
    
    total, basket_items = _basket_totals(basket)
    grand_total = total
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        payment_intent_id = request.POST.get('payment_intent_id')
        if form.is_valid():
            order = form.save(commit=False)
            try:
                order.total = grand_total
            except Exception:
                pass
            if payment_intent_id:
                try:
                    order.stripe_pid = payment_intent_id
                except Exception:
                    pass
            order.save()
            
            for entry in basket_items:
                OrderLineItem.objects.create(
                    order=order,
                    product=entry['product'],
                    quantity=entry['quantity'],
                    lineitem_total=entry['lineitem_total'],
                )
                
            request.session['basket'] = {}
            messages.success(request, "Your order is in process now!")
            return redirect(reverse('checkout:success'))
        else:
            messages.error(request, "There was an error with your form. Please double check your information.")
    else:
        form = OrderForm()
        
        
    amount = int((grand_total * Decimal('100')).to_integral_value())
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=settings.STRIPE_CURRENCY,
    )
    
    context = {
        'form': form,
        'order_form': form,
        'basket': basket,
        'basket_items': basket_items,
        'total': total,
        'grand_total': grand_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def success(request):
    request.session['basket'] = {}
    return render(request, 'checkout/success.html')

def cancel(request):
    return render(request, 'checkout/cancel.html')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return JsonResponse({'status': 'invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'status': 'invalid signature'}, status=400)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        print(f"Payment was successful for intent {intent['id']}")

    return JsonResponse({'status': 'success'}, status=200)