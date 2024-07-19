from django import template

register = template.Library()

@register.filter
def image_path(product_name):
    return f"bodega/img/{product_name.lower().replace(' ', '-')}.jpeg"