# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-24 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjaman',
            name='Kondisi',
            field=models.CharField(choices=[('Sedang', 'Sedang'), ('Rusak', 'Rusak'), ('Baik', 'Baik')], default=int, max_length=20),
            preserve_default=False,
        ),
    ]