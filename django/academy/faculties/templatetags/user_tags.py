from django.template import Library

register = Library()


@register.simple_tag
def define(value=None):
    return value


@register.simple_tag
def concat_snake_lc(*args: str):
    return '_'.join(arg.lower() for arg in args)

