# Generated by Django 2.0.7 on 2018-07-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_trade_receiving_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='desired_product_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desired_product_title', to='webapp.Product'),
        ),
        migrations.AddField(
            model_name='trade',
            name='offered_product_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offered_product_title', to='webapp.Product'),
        ),
    ]