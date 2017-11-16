# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0004_actividad_levantamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleLevantamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=50)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Actividad')),
                ('levantamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Levantamiento')),
            ],
        ),
        migrations.CreateModel(
            name='SoporteNC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soporte', models.FileField(upload_to='soporteNC')),
                ('descripcion', models.CharField(max_length=50)),
                ('detalleLevantamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.DetalleLevantamiento')),
            ],
        ),
    ]
