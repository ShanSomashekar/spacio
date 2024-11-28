from django import template

register = template.Library()

@register.filter
def getattr(obj, attr):
    """
    Custom template filter to get an attribute from an object.
    Usage: {{ obj|getattr:"attr_name" }}
    """
    try:
        return getattr(obj, attr)
    except AttributeError:
        return None



from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Custom filter to get value by key (used for row data and primary key)."""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Custom template filter to get an item from a dictionary.
    """
    return dictionary.get(key)
