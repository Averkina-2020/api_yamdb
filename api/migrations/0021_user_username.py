# Generated by Django 3.0.5 on 2021-02-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210225_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='username'),
        ),
    ]
