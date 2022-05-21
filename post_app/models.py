
from django.db import models

class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=255, verbose_name='названия')
    descriptions = models.TextField(verbose_name='Описания')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')
    # director = models.ManyToManyField(blank=True, verbose_name='Директории')
    def __str__(self):
        return self.title

class Director(models.Model):
    class Meta:
        verbose_name = 'Директория'
        verbose_name_plural = 'Директории'
    director = models.CharField(max_length=155, verbose_name='имя')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
    def __str__(self):
        return self.director



class Movie_commits(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    author = models.CharField(max_length=12, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')



class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
