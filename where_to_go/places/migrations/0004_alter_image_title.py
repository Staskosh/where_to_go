# Generated by Django 4.0.3 on 2022-04-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_placeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Координаты'),
        ),
    ]
