# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='emergency',
            field=models.BooleanField(verbose_name='emergency?', default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(verbose_name='邮箱', blank=True, max_length=254, null=True),
        ),
    ]
