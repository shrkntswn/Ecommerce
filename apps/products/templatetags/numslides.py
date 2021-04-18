from django import template

register = template.Library()

@register.filter(name='numslides')
def numslides(number):
    return range(number)
