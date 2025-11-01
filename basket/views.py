from django.shortcuts import redirect, render, get_object_or_404
from marketplace.models import Product

def add_to_basket(request, product_id):
    basket = request.session.get('basket', {})
    basket[str(product_id)] = basket.get(str(product_id), 0) + 1
    request.session['basket'] = basket
    return redirect('view_basket')

def view_basket(request):
    basket = request.session.get('basket', {})
    products = []
    total = 0
    
    for product_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=product_id)
        product.quantity = quantity
        product.subtotal = product.price * quantity
        total += product.subtotal
        products.append(product)
        
    return render(request, 'basket/basket.html', {'products': products, 'total': total})
