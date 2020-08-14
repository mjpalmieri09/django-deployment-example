from django import template

register = template.Library()

@register.filter(name='cut')
def  cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)        # first param is what we will call it, second param is refeerence to function above
