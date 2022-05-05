from django import forms
from django.forms import ModelForm

from TrustApp.models import Profile
from TrustApp.models import User, Title

possibleTitles = Title.objects.all()

class NewEmployeeForm(ModelForm):
    firstName = forms.CharField(max_length="50")
    lastName = forms.CharField(max_length="50")
    email = forms.CharField(max_length="50")
    jobTitle = forms.ChoiceField(choices=possibleTitles)
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']
    