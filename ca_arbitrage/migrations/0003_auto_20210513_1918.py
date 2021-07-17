# Generated by Django 3.1.1 on 2021-05-13 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ca_arbitrage', '0002_auto_20210513_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_tracking_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trading',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_trading_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usersbalance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_balance_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userskeys',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_keys_name', to=settings.AUTH_USER_MODEL),
        ),
    ]