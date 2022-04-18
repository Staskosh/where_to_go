from io import BytesIO

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
        def download_file(place_url):
            response = requests.get(place_url)
            response.raise_for_status()
            return response.json()

        raw_place = download_file(options['place_url'][0])

        def upload_place_to_db(place_info):
            place = Place.objects.get_or_create(
                title=place_info['title'],
                description_short=place_info['description_short'],
                description_long=place_info['description_long'],
                placeid=translit(place_info['title'], reversed=True),
                lng=float(place_info['coordinates']['lng']),
                lat=float(place_info['coordinates']['lat'])
            )
            place[0].save()

            all_images = place[0].image.count()
            image_links = place_info['imgs']
            for image_link in image_links:
                image_name = image_link.split('/')[-1]
                response = requests.get(image_link)
                response.raise_for_status()
                buf = BytesIO()
                buf.write(response.content)
                image = Image.objects.get_or_create(
                    number=all_images+1,
                    title=place[0],
                    img=File(buf, image_name)
                )
                image[0].save()

        upload_place_to_db(raw_place)
