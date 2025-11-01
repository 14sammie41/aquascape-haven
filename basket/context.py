def basket_item_count(request):
    """
    A context processor to add the total number of items in the basket
    to the context of every template.
    """
    basket = request.session.get('basket', {})
    total_items = sum(basket.values())
    return {'basket_count': total_items}