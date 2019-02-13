from django.shortcuts import render

from django.db.models import Q

from Countries.models import Countries
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.



def printHome(request):

    #get all countries

    countries = Countries.objects.all()
    # get the top 10 scores
    top_countries = list((Countries.objects.order_by('-rate').values_list('rate', flat=True).distinct()))

    # get the names of the top 10 scores
    top_records = (Countries.objects.order_by('-rate').filter(rate__in=top_countries[:6]))

    context_top = {"top_countries": top_records , "all_countries" : countries}

    return render(request , 'Home.html' , context_top)
