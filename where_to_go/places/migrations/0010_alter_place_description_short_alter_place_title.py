# Generated by Django 4.0.3 on 2022-04-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_description_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
