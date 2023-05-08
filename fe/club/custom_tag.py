from django import template

register = template.Library()

@register.simple_tag
def div(a, b):
    return int(a / b)