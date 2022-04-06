import json

from django.conf import settings
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from places.models import Place


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response = HttpResponse(place.title)

    images = ["{0}{1}".format(settings.MEDIA_URL, image.img) for image in place.image.all()]
    coordinates = place.coordinates.first()
    print([image.img.file for image in place.image.all()])
    json_response = JsonResponse({
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': coordinates.lng,
            'lat': coordinates.lat
        }
    }, json_dumps_params={'indent': 2, 'ensure_ascii': False})

    return json_response

def show_places(request):
    places = Place.objects.all()
    places_geo = {
        "type": "FeatureCollection",
        "features": '',
    }
    places_feature = []
    for place in places:
        title = place.title
        print(title)
        placeid = place.placeid
        coordinates = place.coordinates.first()
        places_feature.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [coordinates.lng, coordinates.lat]
            },
            "properties": {
                "title": title,
                "placeId": placeid,
                "detailsUrl": f'./static/places/{placeid}.json'
            }
        })
    places_geo['features'] = places_feature

    context = {
        'places_json': places_geo
    }
    return render(request, 'index.html', context)

# Create your views here.
