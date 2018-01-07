# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=100, help_text='Enter the project name')),
                ('color', models.CharField(max_length=7, verbose_name='color', help_text='Enter the hex color code, like #ccc or #cccccc', default='#fff', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|#[0-9a-fA-F]')])),
                ('user', models.ForeignKey(to='taskmanager.Profile', verbose_name='user', related_name='projects')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ('user', 'name'),
                'verbose_name': 'Project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
