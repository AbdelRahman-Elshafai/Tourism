from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Admin
# Create your views here.


def printAdmin(request):

    return HttpResponse("Hello Admin")