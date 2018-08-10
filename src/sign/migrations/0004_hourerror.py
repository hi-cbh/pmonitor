# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-06 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_error'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField()),
                ('times', models.TextField()),
                ('testcaseonbtnlogin', models.IntegerField()),
                ('testcaselogin', models.IntegerField()),
                ('testcasesendnoattach', models.IntegerField()),
                ('testcasesendattach', models.IntegerField()),
                ('testcasefwdsend', models.IntegerField()),
                ('testcaseforward', models.IntegerField()),
                ('testcasereply', models.IntegerField()),
                ('testdownfile', models.IntegerField()),
                ('testcasecheckaddresslist', models.IntegerField()),
                ('testcaseselected', models.IntegerField()),
                ('testcasepush', models.IntegerField()),
                ('testcasecalendar', models.IntegerField()),
                ('testcasediscover', models.IntegerField()),
                ('testcasepersionmessages', models.IntegerField()),
                ('testcaseskydrive', models.IntegerField()),
            ],
        ),
    ]