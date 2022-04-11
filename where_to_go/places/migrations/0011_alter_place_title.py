# Generated by Django 4.0.3 on 2022-04-11 07:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_description_short_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=tinymce.models.HTMLField(max_length=200, verbose_name='Заголовок'),
        ),
    ]