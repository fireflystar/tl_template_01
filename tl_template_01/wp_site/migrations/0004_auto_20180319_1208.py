# Generated by Django 2.0.3 on 2018-03-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wp_site', '0003_auto_20180309_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpposts',
            name='post_category',
            field=models.IntegerField(blank=True, choices=[(1, '人工智能'), (2, '区块链'), (3, '大数据')], null=True),
        ),
    ]
