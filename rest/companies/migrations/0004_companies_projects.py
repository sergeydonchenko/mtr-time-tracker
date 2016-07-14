# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('companies', '0003_auto_20160713_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='projects',
            field=models.ManyToManyField(blank=True, null=True, to='projects.Projects', verbose_name='Projects'),
        ),
    ]