# Generated by Django 3.2.23 on 2023-12-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile.png', upload_to='userprofile/'),
        ),
    ]
