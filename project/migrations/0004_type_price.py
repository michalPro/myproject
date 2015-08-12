# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150811_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=2),
        ),
    ]
