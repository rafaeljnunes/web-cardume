# Generated by Django 2.0.7 on 2018-07-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180708_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
