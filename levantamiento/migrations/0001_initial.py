# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametrizacion', '0004_auto_20171114_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoyo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Empresa')),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Convenio')),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.AddField(
            model_name='apoyo',
            name='circuito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Circuito'),
        ),
    ]
