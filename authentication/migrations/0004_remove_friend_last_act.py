# Generated by Django 3.2.6 on 2021-08-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_friend_last_act'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='last_act',
        ),
    ]
