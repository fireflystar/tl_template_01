from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe

from wp_site.models import WpPosts

register = template.Library()


@register.simple_tag
def title(id):
    a_tag = []
    articles = WpPosts.objects.only('id', 'post_title', 'post_category').filter(post_category=int(id)).filter(
        post_date__lt=timezone.now()).order_by('-post_date')
    if articles.count() > 8:
        articles = articles[:8]
    for article in articles:
        a_tag.append('<li class="list-group-item"><a href="/%s/%s.html">%s</a></li>' %
                     (article.get_post_category_display(), article.id, article.post_title))
    return mark_safe(''.join(a_tag))


@register.simple_tag
def hot():
    a_tag = []
    articles = WpPosts.objects.only('id', 'post_title', 'post_category', 'post_read').filter(post_read__gt=0).order_by(
        '-post_read')
    if articles.count() > 8:
        articles = articles[:8]
    for article in articles:
        a_tag.append('<li class="list-group-item"><a href="/%s/%s.html">%s</a></li>' %
                     (article.get_post_category_display(), article.id, article.post_title))
    return mark_safe(''.join(a_tag))
