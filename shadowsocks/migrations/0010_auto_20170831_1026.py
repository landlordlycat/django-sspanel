# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0009_invitecode_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecode',
            name='type',
            field=models.IntegerField(choices=[(1, '公开'), (0, '不公开')], default=0, verbose_name='类型'),
        ),
    ]