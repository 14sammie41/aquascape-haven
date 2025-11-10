from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def calc_subtotal(price, quantity):
    """Calculate the subtotal for a given price and quantity."""
    try:
        return (price * Decimal(quantity))
    except Exception:
        return Decimal('0.00')