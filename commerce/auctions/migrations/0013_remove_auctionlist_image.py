# Generated by Django 5.0.7 on 2024-07-31 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlist',
            name='image',
        ),
    ]