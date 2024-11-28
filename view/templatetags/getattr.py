from django import template

register = template.Library()

@register.filter(name='getattr')
def getattr_filter(obj, attr):
    try:
        return getattr(obj, attr)
    except AttributeError:
        return None
