# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user',
            field=models.OneToOneField(to='polls.User'),
        ),
    ]
