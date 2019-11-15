from django import forms
from . models import UserProfiles
from django.core.exceptions import ValidationError


class Signup(forms.Form):

    name= forms.CharField(label=' NAME:',widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100)
    username = forms.CharField(label='ENTER YOUR USERNAME:', widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100, required=True)
    mail = forms.CharField(label='ENTER YOUR EMAIL ID:', widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100, required=True)
    password= forms.CharField(label='PASSWORD',widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width:400px'}), required=True)
    conpass= forms.CharField(label='CONFIRM PASSWORD',widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width:400px'}), required=True)

    class Meta:
        model = UserProfiles;