# Generated by Django 3.2.6 on 2021-11-08 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_userinfo_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='profile_img',
        ),
    ]
