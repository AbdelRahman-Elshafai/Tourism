# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-20 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_username', models.CharField(max_length=200)),
                ('admin_password', models.CharField(max_length=200)),
            ],
        ),
    ]
