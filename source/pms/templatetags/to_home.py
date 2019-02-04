from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name='to_home')
@stringfilter
def to_home(value):
    return value.replace("/add-vuln/", "/home/")
