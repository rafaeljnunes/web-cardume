# Generated by Django 2.0.7 on 2018-07-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='', max_length=140),
        ),
    ]
