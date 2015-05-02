# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150429_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
