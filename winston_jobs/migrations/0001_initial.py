# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('val', models.TextField(blank=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winston_jobs.Job')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winston_jobs.Job'),
        ),
        migrations.AlterUniqueTogether(
            name='keyval',
            unique_together=set([('job', 'key')]),
        ),
    ]
