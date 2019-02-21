from django.shortcuts import render , redirect

from .models import Countries , Cities , Locations , Experience , Comments
from .forms import ExperienceForm ,CommentForm
from Profile.models import Users
from django.http import HttpResponse , HttpResponseRedirect
import datetime

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


    countries = Countries.objects.all()

    city_info=Cities.objects.get(city_name=city_name)

    city_id=city_info.city_ID
    locations_info=Locations.objects.filter(city_ID=city_id)


    context = {'city_info': city_info,'locations_info':locations_info , 'all_countries': countries}

    # from session
    user = request.user
    user_id = user.id
    user_instance = Users.objects.get(id=user_id)
    user_name =user_instance.username
    city_instance = Cities.objects.get(city_ID=city_id)
    date = datetime.datetime.now()

    #Experience Form
    experienceForm = ExperienceForm(request.POST or None)
    if experienceForm.is_valid():

        if user.is_authenticated():

            # see if he is blocked and lock him out
            if user.blk_flg == True:

                return render(request, 'BlkMsg.html')
        description =experienceForm.cleaned_data['Leave_your_Experience']

        experience_data=Experience(user_ID=user_instance,city_ID=city_instance,date=date,description=description)

        experience_data.save()

        url = '/Tourism/'+ country_name + "/" + city_name + "/"
        return redirect(url)

    allExperience=Experience.objects.filter(city_ID=city_id)
    experience_count=Experience.objects.filter(city_ID=city_id).count()


    allComments=Comments.objects.all()
    comment_count=Comments.objects.all().count()


    context = {'all_countries':countries,'city_info': city_info,'locations_info':locations_info,
               'ExperienceForm':experienceForm,'allExperience':allExperience,'experience_count':experience_count,'user_name':user_name,
               'allComments':allComments,'comment_count':comment_count , 'country_name' : country_name}

    return render(request,'city.html',context)


def addComment(request,country_name , city_name , exper_ID):
    countries = Countries.objects.all()

    #from sesstion
    user = request.user
    user_id= user.id
    user_instance=Users.objects.get(id=user_id)
    experience_instance = Experience.objects.get(exper_ID=exper_ID)
    date = datetime.datetime.now()

    #Comment Form
    commentForm=CommentForm(request.POST or None)
    if commentForm.is_valid():

        if user.is_authenticated():

            # see if he is blocked and lock him out
            if user.blk_flg == True:
                return render(request, 'BlkMsg.html')

        description=commentForm.cleaned_data['reply']

        comment_data=Comments(user_ID=user_instance,date=date,exper_ID=experience_instance,description=description)

        comment_data.save()
        # context={'exper_ID':exper_ID}
        # return render(request, 'city.html', context)

        url = '/Tourism/'+ country_name + "/" + city_name + "/"
        return redirect(url)


    context={'all_countries':countries,'commentForm':commentForm}

    return render(request,'comment.html',context)