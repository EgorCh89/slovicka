from django import template
from page.models import *
from views import recent_dicts
register = template.Library()

@register.simple_tag
def get_my_dicts(requset):
    return recent_dicts(requset)