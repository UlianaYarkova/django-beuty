from django.db import models


class Feedback(models.Model):
    username = models.CharField(verbose_name='Никнейм',max_length=255)
    content = models.TextField(verbose_name='Отзыв')
    grade = models.CharField(verbose_name='Оценка', max_length=255)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'