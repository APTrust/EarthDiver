# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='exp_fixity',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
    ]
