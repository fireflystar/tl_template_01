from django import template
from django.utils.safestring import mark_safe

from wp_site.models import GlobalAnchor

register = template.Library()


def process_anchor_text(text, key_word, link):
    """
    此函数给文章加锚文本
    :param text: 待处理文本
    :param key_word: 单个关键词
    :param link: 关键词对应链接
    :return: 处理结束的文本
    """
    try:
        assert type(text) == str
    except AssertionError:
        return text
    return text.replace(key_word, '<a href="%s">%s</a>' % (link, key_word))


@register.simple_tag
def set_anchor(text):
    global_anchors = GlobalAnchor.objects.filter(is_enable=True).all()
    if global_anchors:
        for anchor in global_anchors:
            text = process_anchor_text(text, anchor.key_word, anchor.link)
    return mark_safe(text)
