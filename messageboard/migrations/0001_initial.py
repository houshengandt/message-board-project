# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('message', models.CharField(max_length=500, verbose_name='留言')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='留言时间')),
            ],
        ),
    ]
