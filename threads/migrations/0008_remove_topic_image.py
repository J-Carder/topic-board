# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0007_auto_20170618_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='image',
        ),
    ]
