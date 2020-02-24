# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-29 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_auto_20180606_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='language',
            field=models.CharField(choices=[(b'gre', b'Greek'), (b'eng', b'English')], default=b'gre', help_text='language used within the dataset', max_length=3, verbose_name='language'),
        ),
    ]
