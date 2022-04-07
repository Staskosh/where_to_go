from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    placeid = models.CharField('Название места', max_length=200, blank=True)
    lng = models.FloatField('Долгота', blank=True, null=True)
    lat = models.FloatField('Широта', blank=True, null=True)

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
# Create your models here.
