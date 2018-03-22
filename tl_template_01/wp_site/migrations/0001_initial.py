# Generated by Django 2.0 on 2018-03-09 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anchor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=64, verbose_name='关键字')),
                ('link', models.CharField(help_text='形如: http://www.baidu.com，不能缺少http://', max_length=1024, verbose_name='链接地址')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalAnchor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=64, verbose_name='关键字')),
                ('link', models.CharField(help_text='形如: http://www.baidu.com，不能缺少http://', max_length=1024, verbose_name='链接地址')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '全局锚文本',
                'verbose_name_plural': '全局锚文本',
            },
        ),
        migrations.CreateModel(
            name='Tdk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.IntegerField(choices=[(1, '主页'), (2, '二级标题页'), (3, '三级标题页'), (4, '文章详情页面')], default=1, verbose_name='页面等级')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='标题T')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='描述D')),
                ('key', models.CharField(blank=True, max_length=128, null=True, verbose_name='关键字K')),
            ],
            options={
                'verbose_name': '全局TDK',
                'verbose_name_plural': '全局TDK',
            },
        ),
        migrations.CreateModel(
            name='WpPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_author', models.CharField(blank=True, max_length=32, null=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_date_gmt', models.DateTimeField(blank=True, null=True)),
                ('post_title', models.CharField(max_length=128)),
                ('post_content', models.TextField()),
                ('post_status', models.IntegerField(blank=True, choices=[(1, '定时'), (2, '立即'), (3, '草稿')], null=True)),
                ('comment_status', models.BooleanField(default=True)),
                ('post_category', models.IntegerField(blank=True, choices=[(1, '栏目1'), (2, '栏目2'), (3, '栏目3')], null=True)),
                ('post_read', models.IntegerField(default=0)),
                ('is_enable', models.BooleanField(default=True)),
                ('disable_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
                'db_table': 'wp_posts',
            },
        ),
    ]
