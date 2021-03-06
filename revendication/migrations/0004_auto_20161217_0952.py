# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-17 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0003_profile_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='organisation',
        ),
        migrations.AddField(
            model_name='organisation',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Profile'),
        ),
    ]
