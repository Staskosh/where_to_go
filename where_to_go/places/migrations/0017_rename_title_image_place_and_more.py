# Generated by Django 4.0.3 on 2022-05-04 12:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_auto_20220504_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='place',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default=' ', verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default=' ', verbose_name='Краткое описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(default=0, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]