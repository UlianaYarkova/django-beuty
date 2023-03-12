from django.db import models

class Master(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    biography = models.TextField(verbose_name='о себе')
    photo = models.ImageField(verbose_name='фото', upload_to='masters')
    experience = models.CharField(verbose_name='Стаж', max_length=255)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'