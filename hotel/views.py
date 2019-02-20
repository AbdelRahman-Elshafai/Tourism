from django.shortcuts import render

from Countries.models import Cities, Locations
from Profile.models import User
from hotel.models import Hotel , HotelReservationRequest
from .forms import ReserveForm
from django.http import HttpResponseRedirect
# Create your views here.


# def reservation(request):
#     form = reservationForm()
#     if request.method == "POST":
#         form = reservationForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()
#     return render(request, 'hotel.html', {'form':form})


def reservation(request):

    form = ReserveForm(request.POST or None)


    if form.is_valid():

        #user id will be in session
        user_id = 1

        # get Hotel id from value selected
        hotel_id = form.cleaned_data['hotels']

        #get the number of adults from the value selected

        no_adults = form.cleaned_data['no_adults']

        # From date
        from_date = form.cleaned_data['from_date']

        # To date
        to_date = form.cleaned_data['to_date']

        # create an instance of the Hotel cuz it's a foreign key by using the id
        hotel_instance = Hotel.objects.get(hotel_id=eval(hotel_id))

        # create instance of the user cuz it's a foreign key by using his id
        user_instance = User.objects.get(user_id=user_id)

        # using the instance make the row and use date() to get the date only not the time
        reservation = HotelReservationRequest(from_date=from_date.date() , to_date = to_date.date(), no_of_adults=no_adults,hotel_id=hotel_instance , user_id=user_instance )

        print(hotel_instance)
        # insert into database
        reservation.save()

        return HttpResponseRedirect("/hotel/book")
    else:

        # get the id of the city

        city_id = Cities.objects.only('city_ID').get(city_name='al-Iskandariyah').city_ID

        # get all the locations names and id's related to that city

        hotels = Hotel.objects.values_list('hotel_name' ,  'hotel_id').filter(city_id=city_id)

        #populate the choices of the select form

        choices = []
        for loc , id in hotels:
            choices += ((int(id),) + (loc,),)

        form.fields['hotels'].choices = choices


        return render(request , 'book.html' , {"book_form" : form })
