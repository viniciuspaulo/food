from django.shortcuts import render
from .models import Category
from .models import Company

import json
from yelpapi import YelpAPI

from django.http import JsonResponse

from django.db.models import Q

def index(request):
    companys = []
    search = request.GET.get('q')
    if (search):
        companys = Company.objects.filter(Q(name__contains=search) | Q(localizacao__contains=search))
    else:
        companys = Company.objects.all()
    sort = request.GET.get('sort')
    if (sort):
        companys = companys.order_by(sort)

    categories = Category.objects.all()
    return render(request,"food/index.html",{
        "categories": categories,
        "companys": companys,
        "search": search
    })


def yielpCapture(request):

    yelp_api = YelpAPI("nL3ET4c4CnqkoWGNJdED7U2TDRd8tEchR7S7hypOB4MohECNJHdJKbjt4lb7okvtuwHX1eVe3GO6SLlpeF8L2MZZOBbL_3HVnkTwXmFvj6-_sWS61P9ea8zsAJ1cXHYx")
    search_results = yelp_api.search_query(
        term='Centro', 
        location='São paulo, SP',
        limit=50
    )

    Company.objects.all().delete()
    for business in search_results['businesses']:
        company = Company(
            photo_yelp=business['image_url'], 
            rating_yelp=business['rating'], 
            
            name=business['name'], 
            email=business['alias']+"@email.com",
            localizacao=business['location']["address1"]+business['location']["city"]+business['location']["state"],
            lat=business['coordinates']['latitude'], 
            lng=business['coordinates']['longitude']
        )
        company.save(force_insert=True)

    return JsonResponse(search_results)
