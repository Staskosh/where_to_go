import json

from django.shortcuts import render
from django.template.response import TemplateResponse

from places.models import Place


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
    print(places_geo)

    context = {
        'places_json': places_geo
    }
    return render(request, 'index.html', context)

# Create your views here.
