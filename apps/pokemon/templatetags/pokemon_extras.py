from django import template

register = template.Library()

@register.filter()
def to_upper(text):
    return text.upper()