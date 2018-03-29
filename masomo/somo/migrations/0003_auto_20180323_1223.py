# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('somo', '0002_auto_20180322_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees', models.IntegerField(null=True)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='somo.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Marks',
        ),
    ]
