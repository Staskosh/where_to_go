import json

from django.shortcuts import render
from django.template.response import TemplateResponse

from places.models import Place


places_geo = {
        "type": "FeatureCollection",
        "features": '',
    }


def show_places(request):
    # places = Place.objects.all()
    # places_feature = []
    # for place in places:
    #     title = place.title
    #     print(title)
    #     placeid = place.placeid
    #     coordinates = place.coordinates.first()
    #     # images = place.image.all()
    #     # image_urls = [image for image in images]
    #     places_feature.append({
    #         "type": "Feature",
    #         "geometry": {
    #             "type": "Point",
    #             "coordinates": [coordinates.lat, coordinates.lng]
    #         },
    #         "properties": {
    #             "title": title,
    #             "placeId": placeid,
    #             "detailsUrl": f'./static/places/{placeid}.json'
    #         }
    #     })
    # places_geo['features'] = places_feature
    # print(places_geo)

    places_geo = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "./static/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "./static/places/roofs24.json"
          }
        }
      ]
    }

    context = {
        'places_json': places_geo
    }
    return render(request, 'index.html', context)

# Create your views here.
