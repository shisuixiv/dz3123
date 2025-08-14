from django.db import models

class Library(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовк'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    date = models.DateField(
        verbose_name='Дата выхода'
    )
    author = models.CharField(
        max_length=60,
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title