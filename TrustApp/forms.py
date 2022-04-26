from django import forms
from django.forms import ModelForm

from TrustApp.models import Profile
from TrustApp.models import User

possibleTitles = ("Domestic Violence Advocate", "Sr Manager", "Therapist", "Corp Manager", "CEO")
possibleUserRoles = ("Employee", "Manager", "Admin")

class NewEmployeeForm(ModelForm):
    firstName = forms.CharField(max_length="50")
    lastName = forms.CharField(max_length="50")
    email = forms.CharField(max_length="50")
    jobTitle = forms.ChoiceField(choices=possibleTitles)
    userRoles = forms.ChoiceField(choices=possibleUserRoles)
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']
    