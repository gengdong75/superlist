# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
