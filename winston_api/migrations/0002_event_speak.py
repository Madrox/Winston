# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winston_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='speak',
            field=models.BooleanField(default=False),
        ),
    ]