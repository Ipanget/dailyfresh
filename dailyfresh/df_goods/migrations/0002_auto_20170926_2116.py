# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='goods_status_choice',
            new_name='goods_status',
        ),
    ]
