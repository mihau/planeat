# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('weight', models.FloatField()),
                ('edible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Edible')),
            ],
        ),
    ]