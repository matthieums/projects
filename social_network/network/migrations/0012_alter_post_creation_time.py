# Generated by Django 5.0.3 on 2024-04-17 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_user_photo_url_alter_post_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.TimeField(default=datetime.time(15, 49, 33, 46941)),
        ),
    ]
