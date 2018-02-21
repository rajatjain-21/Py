# Generated by Django 2.0 on 2018-02-16 04:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 2, 16, 4, 59, 36, 774834, tzinfo=utc))),
            ],
        ),
    ]
