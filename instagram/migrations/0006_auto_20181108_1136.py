# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20181108_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Comments',
            new_name='comments',
        ),
    ]
