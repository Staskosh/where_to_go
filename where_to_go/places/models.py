from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField('Позиция', default=0)
    title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='image',
        verbose_name='Координаты',
    )
    img = models.ImageField('Картинка')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.title.title}'
