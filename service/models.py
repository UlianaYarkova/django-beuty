from django.db import models
from master.models import Master
from authentication.models import User

class Service(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=255)
    master = models.ManyToManyField(verbose_name='Мастера',to=Master, related_name='services')
    price = models.CharField(verbose_name='Цена', max_length=255) 
    cover = models.ImageField(verbose_name='Обложка', upload_to='cover/photos')
    time = models.CharField(verbose_name='Продолжительность', max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class FavoriteService(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Service', on_delete=models.CASCADE)