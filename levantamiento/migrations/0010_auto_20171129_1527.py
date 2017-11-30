# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0009_auto_20171128_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='soporte',
            field=models.FileField(null=True, upload_to='soporteLEV'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Estado'),
        ),
    ]