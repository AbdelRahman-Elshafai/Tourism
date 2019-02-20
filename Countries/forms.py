from django import forms
from .models import Experience , Comments
from django.forms import TextInput



class ExperienceForm(forms.Form):
     Leave_your_Experience=forms.CharField(widget=forms.Textarea)

     def __init__(self, *args, **kwargs):
          super(ExperienceForm, self).__init__(*args, **kwargs)

          # override the id and class to match the css
          self.fields['Leave_your_Experience'].widget = forms.Textarea(attrs={
               'id': 'message',
               'class': 'form-control',
               'placeholder': 'Write your Experience...'})


class CommentForm(forms.Form):
     reply=forms.CharField(widget=forms.Textarea)

     def __init__(self, *args, **kwargs):
          super(CommentForm, self).__init__(*args, **kwargs)

          # override the id and class to match the css
          self.fields['reply'].widget = forms.Textarea(attrs={
               # 'id': 'message',
               # 'class': 'form-control',
               # 'rows':'1',
               # 'cols':'50',
               'placeholder': 'Comment...'})