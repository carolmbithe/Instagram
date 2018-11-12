from .models import Image,Profile
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['profile','pub_date','name','likes','comments']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
