# Generated by Django 3.0.5 on 2021-03-02 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_merge_20210301_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='api.Category', verbose_name='Категория'),
        ),
    ]
