# Generated by Django 2.2.5 on 2019-09-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190905_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='full_descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Подробное описание'),
        ),
    ]
