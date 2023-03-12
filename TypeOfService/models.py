from django.db import models
from service.models import Service

class TypeOfService(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    services = models.ManyToManyField(verbose_name='Услуги', to=Service,related_name='types')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'