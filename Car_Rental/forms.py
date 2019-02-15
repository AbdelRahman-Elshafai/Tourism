from django import forms
from django.forms import fields_for_model
from Countries.models import Countries

TOPIC_CHOICES = (('general', 'General enquiry'), ('bug', 'Bug report'), ('suggestion', 'Suggestion'),)
country_list = Countries.objects.all()

class ContactForm (forms.Form):
    topic = forms.ChoiceField(choices=country_list)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)


