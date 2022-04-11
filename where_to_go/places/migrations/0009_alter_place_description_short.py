# Generated by Django 4.0.3 on 2022-04-08 12:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(verbose_name='Краткое описание'),
        ),
    ]
