from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=300,
        help_text='Укажите жанр',
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=100,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']
