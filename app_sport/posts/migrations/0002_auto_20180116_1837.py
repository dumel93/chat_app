# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-16 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
    ]
