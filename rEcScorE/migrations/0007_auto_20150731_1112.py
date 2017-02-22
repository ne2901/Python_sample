# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0006_auto_20150731_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 12, 18, 723448, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 12, 18, 723543, tzinfo=utc), null=True, blank=True),
        ),
    ]
