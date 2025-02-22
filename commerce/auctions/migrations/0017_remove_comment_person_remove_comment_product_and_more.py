# Generated by Django 5.0.7 on 2024-08-16 10:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='person',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='person',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='product',
        ),
        migrations.AddField(
            model_name='auctionlist',
            name='comment',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='auctionlist',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='auctions.auctionlist')),
            ],
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]
