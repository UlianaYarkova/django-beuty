# Generated by Django 4.1.7 on 2023-03-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('cover', models.ImageField(upload_to='cover/photos', verbose_name='Обложка')),
                ('time', models.CharField(max_length=255, verbose_name='Продолжительность')),
                ('master', models.ManyToManyField(related_name='services', to='master.master', verbose_name='Мастера')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]