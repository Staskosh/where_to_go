from io import BytesIO
from os.path import split, splitext
from urllib.parse import urlsplit, unquote

import requests
from django.core.files import File
from django.core.management.base import BaseCommand
from places.models import Image, Place
from transliterate import translit


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "place_url",
            nargs='+',
            help="Please enter the url of the file"
        )

    def handle(self, *args, **options):
        response = requests.get(options['place_url'][0])
        response.raise_for_status()
        raw_place = response.json()

        place = Place.objects.get_or_create(
            title=raw_place['title'],
            description_short=raw_place['description_short'],
            description_long=raw_place['description_long'],
            placeid=translit(raw_place['title'], reversed=True),
            lng=float(raw_place['coordinates']['lng']),
            lat=float(raw_place['coordinates']['lat'])
        )

        all_images = place[0].image.count()
        image_links = raw_place['imgs']
        for image_link in image_links:
            _, raw_image_name = split(urlsplit(image_link).path)
            image_name = unquote(raw_image_name)
            response = requests.get(image_link)
            response.raise_for_status()
            buf = BytesIO()
            buf.write(response.content)
            Image.objects.get_or_create(
                number=all_images+1,
                title=place[0],
                img=File(buf, image_name)
            )
