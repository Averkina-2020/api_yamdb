# Generated by Django 3.0.5 on 2021-02-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
    ]