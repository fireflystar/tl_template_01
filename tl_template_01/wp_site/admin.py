from django.contrib import admin

from wp_site.models import WpPosts, Tdk, GlobalAnchor, Tag


def open_comment(modeladmin, request, queryset):
    queryset.update(comment_status=True)


def close_comment(modeladmin, request, queryset):
    queryset.update(comment_status=False)


def set_enable(modeladmin, request, queryset):
    queryset.update(is_enable=True)


def set_disable(modeladmin, request, queryset):
    queryset.update(is_enable=False)


open_comment.short_description = '批量开放评论'
close_comment.short_description = '批量关闭评论'
set_enable.short_description = '批量启用文章'
set_disable.short_description = '批量禁用文章'

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'post_date', 'is_enable')
    list_per_page = 20
    actions = [open_comment, close_comment, set_enable, set_disable]


class TdkAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_id', 'title', 'key')


class GlobalAnchorAdmin(admin.ModelAdmin):
    list_display = ('id', 'key_word', 'link', 'is_enable')


admin.site.register(WpPosts, PostAdmin)
admin.site.register(Tdk, TdkAdmin)
admin.site.register(GlobalAnchor, GlobalAnchorAdmin)
admin.site.register(Tag, TagAdmin)
