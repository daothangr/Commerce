# Generated by Django 5.0.7 on 2024-08-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_remove_auctionlist_isactive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
