# Generated by Django 4.1.7 on 2023-03-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.ImageField(upload_to='covers', verbose_name='Обложка')),
                ('services', models.ManyToManyField(related_name='set', to='service.service', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Комплекс',
                'verbose_name_plural': 'Комплексы',
            },
        ),
    ]