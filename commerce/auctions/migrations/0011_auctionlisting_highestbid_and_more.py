# Generated by Django 5.0.3 on 2024-03-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_bid_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='highestbid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='startingbid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='bid',
            table=None,
        ),
    ]