from django import forms
from .models import *

class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto
        exclude = ["fecha"]