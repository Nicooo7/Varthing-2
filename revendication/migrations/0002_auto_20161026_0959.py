# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposition',
            name='champ_lexical',
            field=models.CharField(default='vide', max_length=100000, null=True),
        ),
    ]
