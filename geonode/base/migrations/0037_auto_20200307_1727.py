# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-03-07 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_auto_20200121_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='data_quality_statement',
            field=models.TextField(blank=True, help_text="general explanation of the data producer's knowledge about the lineage of a dataset", max_length=2000, null=True, verbose_name='lineage'),
        ),
    ]
