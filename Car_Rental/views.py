from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
# from .forms import ContactForm

# Create your views here.
def display(request):
    return HttpResponse("This is working")

#
# def testingTemplate(request):
#     #display the relevant template to rent a car...
#     t = get_template("myTest.html")


def contact(request):
    pass
    # if request.method == "POST":
    #     form = ContactForm(method="post")
    # else:
    #     form = ContactForm()
    # return render_to_response('myTest.html', {'form': form})
