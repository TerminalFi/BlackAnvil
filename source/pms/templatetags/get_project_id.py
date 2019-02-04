from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name='get_project_id')
@stringfilter
def get_project_id(value):
    return re.search(r"\d", value).group()
