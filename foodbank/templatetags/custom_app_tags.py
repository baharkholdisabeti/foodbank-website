# Custom Template tag file named "custom_app_tags.py"
from django import template

register = template.Library()

@register.filter
def addstr(s1, s2):
    return str(s1) + str(s2)