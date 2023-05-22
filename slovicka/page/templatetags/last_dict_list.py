from django import template
from page.models import *
register = template.Library()


@register.simple_tag
def get_my_dicts(user_id):
    if not user_id:
        raise template.TemplateSyntaxError('naval id')
    print(Dictionary.objects.all().filter(creator_id=user_id))
    a = Dictionary.objects.all().filter(creator_id=user_id)
    b = []
    for obj in a:
        b.append(obj.name)
    return (b)