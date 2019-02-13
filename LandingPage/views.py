from django.shortcuts import render

from django.db.models import Q

from Countries.models import Countries , Cities
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.



def printHome(request):

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
