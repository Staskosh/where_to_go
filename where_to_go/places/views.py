from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe

from places.models import Place


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = ["{0}{1}".format(settings.MEDIA_URL, image.img) for image in place.image.all()]
    json_response = JsonResponse({
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
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
        places_feature.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeid,
                "detailsUrl": reverse('place_detail_view', args=[place.id])
            }
        })
    places_geo['features'] = places_feature

    context = {
        'places_json': places_geo
    }
    return render(request, 'index.html', context)

# Create your views here.
