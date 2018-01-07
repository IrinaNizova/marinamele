# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20180107_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('user', models.ForeignKey(related_name='tags', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
                'verbose_name': 'Tag',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]
