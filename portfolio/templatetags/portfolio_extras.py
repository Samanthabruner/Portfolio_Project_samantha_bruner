import re
from django import template


register = template.Library()


@register.filter
def split_commas(value):
    if not value:
        return []
    if '\n' in value:
        return [item.strip() for item in value.split('\n') if item.strip()]
    return [item.strip() for item in value.split(',') if item.strip()]