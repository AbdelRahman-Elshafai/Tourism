from django.shortcuts import render


from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.



def printHome(request):

    return render(request , 'Home.html')
