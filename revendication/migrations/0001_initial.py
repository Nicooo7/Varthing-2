# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 09:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autre_utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pays', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_favoris', models.CharField(max_length=200, null=True)),
                ('lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Lieu')),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ennonce', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateField(default=django.utils.timezone.now, null=True)),
                ('champ_lexical', models.CharField(max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proximite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proba', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Autre_utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revendication.Autre_utilisateur')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Soutien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien', models.CharField(choices=[('CR', 'createur'), ('SO', 'soutien')], max_length=2)),
                ('propositions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revendication.Proposition')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='proposition',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Theme'),
        ),
        migrations.AddField(
            model_name='proposition',
            name='supporter',
            field=models.ManyToManyField(null=True, through='revendication.Soutien', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='utilisateurs_proches',
            field=models.ManyToManyField(through='revendication.Proximite', to='revendication.Autre_utilisateur'),
        ),
    ]
