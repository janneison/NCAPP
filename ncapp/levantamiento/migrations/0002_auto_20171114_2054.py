# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('alineacion', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='TipoDato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('comportamiento', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='capitulo',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Version'),
        ),
    ]
