from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    placeid = models.CharField('Название места', max_length=200, blank=True)

    def __str__(self):
        return self.title

class Coordinates(models.Model):
    title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Координаты',
        related_name='coordinates',
    )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title.title}'


class Image(models.Model):
    number = models.IntegerField('Номер фото')
    title = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='image',
        verbose_name='Координаты',
    )
    img = models.ImageField('Фото')

    def __str__(self):
        return f'{self.number} {self.title.title}'



# Create your models here.
