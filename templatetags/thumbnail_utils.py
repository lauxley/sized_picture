from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@stringfilter
def width(size, minus):
    try:
        return int(size.split('x')[0])-int(minus)
    except IndexError, ValueError:
        return 0
register.filter('width', width)

@stringfilter
def height(size, minus):
    try:
        return int(size.split('x')[1])-int(minus)
    except IndexError, ValueError:
        return 0
register.filter('height', height)
