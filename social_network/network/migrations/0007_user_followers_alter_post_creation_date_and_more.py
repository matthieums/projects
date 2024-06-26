# Generated by Django 5.0.3 on 2024-04-10 14:21

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_post_title_alter_post_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(default=datetime.date(2024, 4, 10)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.TimeField(default=datetime.time(14, 21, 31, 910665)),
        ),
    ]
