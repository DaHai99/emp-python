from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def func1(a1, a2, a3):
    return a1 + a2


@register.filter
def func2(a1, a2):
    print(a2, type(a2))
    return a1 + str(a2)
