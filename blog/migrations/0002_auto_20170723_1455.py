# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_type',
            field=models.TextField(null=True),
        ),
    ]
