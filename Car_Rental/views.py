from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response

from Car_Rental.forms import RentalForm

from Countries.models import Locations , Cities

# Create your views here.
# def display(request):
#     return HttpResponse("This is working")

#
# def testingTemplate(request):
#     #display the relevant template to rent a car...
#     t = get_template("myTest.html")


# def contact(request):
#     pass
    # if request.method == "POST":
    #     form = ContactForm(method="post")
    # else:
    #     form = ContactForm()
    # return render_to_response('myTest.html', {'form': form})



def rent(request):


    form = RentalForm(request.POST or None)

    if form.is_valid():

        return HttpResponseRedirect("/Car_Rental/rent")
    else:
        # get the id of the city

        city_id = Cities.objects.only('city_ID').get(city_name='al-Iskandariyah').city_ID

        # get all the locations names and id's related to that city

        locations = Locations.objects.values_list('location_name' ,  'location_ID').filter(city_ID=city_id)

        #populate the choices of the select form
        choices = []
        for loc , id in locations:
            choices += ((id,) + (loc,),)

        print(choices)
        form.fields['location'].choices = choices

        return render(request , 'rent.html' , {"rental_form" : form })
