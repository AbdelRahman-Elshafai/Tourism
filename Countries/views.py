from django.shortcuts import render

from .models import Countries , Cities , Locations
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.



def displayHome(request):

    #get all countries

    countries = Countries.objects.all()

    # get the top 6 countries

    top_countries = list((Countries.objects.order_by('-rate').values_list('rate', flat=True).distinct()))

    # get the names of the top 6 countries

    top_country_records = (Countries.objects.order_by('-rate').filter(rate__in=top_countries[:6]))

    #get all cities

    cities = Cities.objects.all()

    #get top 6 cities

    top_cities = list((Cities.objects.order_by('-rate').values_list('rate', flat=True).distinct()))

    #get names of top 6 cities

    top_city_records = (Cities.objects.order_by('-rate').filter(rate__in=top_cities[:6]))

    top_three_cities = top_city_records[:3]

    next_top_three_cities = top_city_records[3:6]


    context = {"top_countries": top_country_records , "all_countries" : countries , "top_three_cities" : top_three_cities , "next_top_three_cities" : next_top_three_cities , "all_cities" : cities}


    return render(request , 'Home.html' , context)


def showCountry(request,country_name):

    countries = Countries.objects.all()
    country_info=Countries.objects.get(country_name=country_name)

    country_id=country_info.country_ID

    top_cities = list((Cities.objects.filter(country_ID=country_id).order_by('-rate').values_list('rate', flat=True).distinct()))
    top_city_records = (Cities.objects.filter(country_ID=country_id).order_by('-rate').filter(rate__in=top_cities[:6]))
    top_two_cities = top_city_records[:2]
    next_top_two_cities = top_city_records[2:4]
    last_top_two_cities = top_city_records[4:6]
    rest_city_records = (Cities.objects.filter(country_ID=country_id).filter(rate__in=top_cities[6:]))

    context={'country_info':country_info,'top_two_cities':top_two_cities, 'next_top_two_cities':next_top_two_cities ,
             'last_top_two_cities':last_top_two_cities,'rest_city_records':rest_city_records,'all_countries':countries}
    return render(request,'country.html',context)



def showCity(request,city_name,country_name='country'):
    city_info=Cities.objects.get(city_name=city_name)


    city_id=city_info.city_ID
    locations_info=Locations.objects.filter(city_ID=city_id)

    context = {'city_info': city_info,'locations_info':locations_info}

    return render(request,'city.html',context)