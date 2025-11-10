from django.shortcuts import redirect, render, get_object_or_404
from marketplace.models import Product

def add_to_basket(request, product_id):
    basket = request.session.get('basket', {})
    basket[str(product_id)] = basket.get(str(product_id), 0) + 1
    request.session['basket'] = basket
    return redirect('basket:view_basket')

def view_basket(request):
    basket = request.session.get('basket', {})
    products = []
    total = 0
    
    for product_id, qty in basket.items():
        product = get_object_or_404(Product, id=product_id)
        products.append({'product': product, 'quantity': qty})
        total += product.price * qty
        
    return render(request, 'basket/basket.html', {'products': products, 'total': total})
