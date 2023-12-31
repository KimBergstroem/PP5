# Generated by Django 3.2.23 on 2023-12-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_subscribedusers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedusers',
            name='subscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='email',
            field=models.EmailField(max_length=45, unique=True),
        ),
    ]
