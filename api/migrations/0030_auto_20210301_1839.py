# Generated by Django 3.0.5 on 2021-03-01 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_user_is_moderator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tempauth',
            options={},
        ),
        migrations.RemoveField(
            model_name='tempauth',
            name='date',
        ),
    ]
