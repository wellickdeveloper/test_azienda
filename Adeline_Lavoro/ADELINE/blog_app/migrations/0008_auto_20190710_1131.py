# Generated by Django 2.2.1 on 2019-07-10 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20190710_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='data',
            field=models.DateField(default=datetime.datetime(2019, 7, 10, 9, 31, 41, 701116, tzinfo=utc), max_length=30),
        ),
    ]
