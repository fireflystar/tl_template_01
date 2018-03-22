from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=128, null=True, blank=True)

class WpPosts(models.Model):
    post_author = models.CharField(max_length=32, null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_date_gmt = models.DateTimeField(null=True, blank=True)
    post_title = models.CharField(max_length=128)
    post_content = models.TextField()
    status = (
        (1, '定时'),
        (2, '立即'),
        (3, '草稿'),
    )
    post_status = models.IntegerField(choices=status, default=2)
    comment_status = models.BooleanField(default=False)
    category = (
        (1, '人工智能'),
        (2, '区块链'),
        (3, '大数据'),
    )
    post_category = models.IntegerField(choices=category, null=True, blank=True)
    post_read = models.IntegerField(default=0)
    tag_id = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE,)
    is_enable = models.BooleanField(default=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'wp_posts'
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'


class Tdk(models.Model):
    tdk_type = (
        (1, '主页'),
        (2, '二级标题页'),
        (3, '三级标题页'),
        (4, '文章详情页面'),

    )
    type_id = models.IntegerField(choices=tdk_type, verbose_name='页面等级', default=1)
    title = models.CharField(max_length=128, null=True, blank=True, verbose_name='标题T')
    description = models.CharField(max_length=512, null=True, blank=True, verbose_name='描述D')
    key = models.CharField(max_length=128, null=True, blank=True, verbose_name='关键字K')

    class Meta:
        verbose_name = '全局TDK'
        verbose_name_plural = '全局TDK'


class GlobalAnchor(models.Model):
    key_word = models.CharField(max_length=64, verbose_name='关键字')
    link = models.CharField(max_length=1024, verbose_name='链接地址', help_text='形如: http://www.baidu.com，不能缺少http://')
    is_enable = models.BooleanField(default=True, verbose_name='是否启用')

    class Meta:
        verbose_name = '全局锚文本'
        verbose_name_plural = '全局锚文本'


class Anchor(models.Model):
    key_word = models.CharField(max_length=64, verbose_name='关键字')
    link = models.CharField(max_length=1024, verbose_name='链接地址', help_text='形如: http://www.baidu.com，不能缺少http://')
    is_enable = models.BooleanField(default=True, verbose_name='是否启用')



