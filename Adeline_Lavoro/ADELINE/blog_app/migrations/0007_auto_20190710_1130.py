# Generated by Django 2.2.1 on 2019-07-10 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20190710_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='data',
            field=models.DateField(default=datetime.date(2019, 7, 10), max_length=30),
        ),
    ]
