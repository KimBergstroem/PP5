# Generated by Django 3.2.23 on 2023-12-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]