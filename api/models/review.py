from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    text = models.TextField(
        verbose_name='Отзыв',
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='Автор',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review',
        blank=True,
        verbose_name='Произведение',
    )
    score = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Рейтинг'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            ),
        ]
