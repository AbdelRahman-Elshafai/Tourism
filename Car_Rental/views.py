from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response

from Car_Rental.forms import RentalForm

from Car_Rental.models import Car_Reservation

from Profile.models import Users

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



def rent(request , city_name):


    form = RentalForm(request.POST or None)



    if form.is_valid():

        #user id will be in session
        user_id = 1

        # get location id from value selected
        location_id = form.cleaned_data['location']

        # pick up date
        pick = form.cleaned_data['pick']

        # drop off date
        drop = form.cleaned_data['drop']

        # create an instance of the location cuz it's a foreign key by using the id
        location_instance = Locations.objects.get(location_ID=eval(location_id))

        # create instance of the user cuz it's a foreign key by using his id
        user_instance = Users.objects.get(id=user_id)

        # using the instance make the row and use date() to get the date only not the time
        reservation = Car_Reservation(location_ID=location_instance , user_id=user_instance , pick_up=pick.date() , drop_off=drop.date())

        # insert into database
        reservation.save()

        return HttpResponseRedirect("/Tourism/home")
    else:
        # get the id of the city

        city_id = Cities.objects.only('city_ID').get(city_name=city_name).city_ID

        # get all the locations names and id's related to that city

        locations = Locations.objects.values_list('location_name' ,  'location_ID').filter(city_ID=city_id)

        #populate the choices of the select form

        choices = []
        for loc , id in locations:
            choices += ((int(id),) + (loc,),)

        form.fields['location'].choices = choices

        return render(request , 'rent.html' , {"rental_form" : form })





