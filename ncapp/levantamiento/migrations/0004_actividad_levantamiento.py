# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametrizacion', '0004_auto_20171114_1943'),
        ('levantamiento', '0003_defecto_norma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Capitulo')),
                ('tipoDato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.TipoDato')),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
        migrations.CreateModel(
            name='Levantamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('inspeccion', models.IntegerField(default=0)),
                ('poligono', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=500)),
                ('apoyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Apoyo')),
                ('contratista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_contratista', to='parametrizacion.Empresa')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Empresa')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Proyecto')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Municipio')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levantamiento.Version')),
            ],
            options={
                'abstract': False,
                'permissions': (('puede_ver', 'puede ver'),),
            },
        ),
    ]
