# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 16:07
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_auto_20190517_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempmodel',
            name='project',
        ),
        migrations.DeleteModel(
            name='TempModel',
        ),
    ]