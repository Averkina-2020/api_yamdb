# Generated by Django 3.0.5 on 2021-02-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя'),
        ),
    ]
