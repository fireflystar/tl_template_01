from bs4 import BeautifulSoup
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def prettify_text(text, l):
    soup = BeautifulSoup(text, 'lxml')
    length = len(soup.text)
    if length > l:
        return mark_safe(soup.text[:l])
    else:
        return mark_safe(soup.text)
