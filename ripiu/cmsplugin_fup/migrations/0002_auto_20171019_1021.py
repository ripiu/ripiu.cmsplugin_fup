# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-19 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_fup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='width'),
        ),
    ]
