# Generated by Django 3.1.4 on 2021-04-26 05:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weeb', '0005_auto_20210425_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 5, 8, 23, 493782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]