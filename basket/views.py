from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from marketplace.models import Product


def add_to_basket(request, product_id):
    """
    Add a product to the shopping basket.
    """
    basket = request.session.get('basket', {})
    basket[str(product_id)] = basket.get(str(product_id), 0) + 1
    request.session['basket'] = basket
    messages.success(request, "Product added to basket.")
    return redirect('basket:view_basket')


def view_basket(request):
    """
    View the shopping basket.
    """
    basket = request.session.get('basket', {})

    if request.method == "POST":
        product_id = str(request.POST.get("product_id"))
        action = request.POST.get("action")

        if action == "update":
            quantity = int(request.POST.get("quantity", 1))
            if quantity > 0:
                basket[product_id] = quantity
                messages.success(request, "Basket updated.")
            else:
                basket.pop(product_id, None)
                messages.info(request, "Item removed from basket.")
        elif action == "delete":
            basket.pop(product_id, None)
            messages.info(request, "Item removed from basket.")

        request.session["basket"] = basket
        return redirect("basket:view_basket")

    products = []
    total = 0

    for product_id, qty in basket.items():
        product = get_object_or_404(Product, id=product_id)
        products.append({'product': product, 'quantity': qty})
        total += product.price * qty

    return render(request, 'basket/basket.html', {
        'products': products,
        'total': total
    })
