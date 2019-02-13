# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-13 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Countries', '0004_auto_20190213_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='local_name',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
