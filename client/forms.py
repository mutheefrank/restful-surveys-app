from django import forms
from django.contrib.auth.models import User
from models import *

class UserForm(forms.ModelForm):
    """
    form for creating dashboard user
    """

    class Meta:
        model = User
        fields = ['username','email', 'password']
        exclude = ['first_name, last_name']

        widgets = {
            'username':forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'type': 'text',
                'placeholder': ' Username ',
                'required': 'true',
                'data-validation-required-message': 'Please enter your username'
            }),

            'email': forms.TextInput(attrs={
                'class':'form-control',
                'id':'email',
                'type':'email',
                'placeholder':'Email Address',
                'required':'true',
                'data-validation-required-message' : 'Please enter your email address.'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'required': 'true',
                'placeholder': 'Password',
                'data-validation-required-message': 'Please enter your passoword'
            }),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_active = True
        user.save()

class LocationForm(forms.ModelForm):
    """
    form for adding locations
    """
    class Meta:
        model = Location
        fields = ['location']
        widgets = {'location' : forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'location ',
            'required': 'true',
        })}

class DrinkForm(forms.ModelForm):
    """
    form for adding drink varieties
    """
    class Meta:
        model = Drink
        fields = ['drink']
        widgets = {'drink' : forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'drink ',
            'required': 'true',
        })}


class SurveyForm(forms.ModelForm):
    """
    form for capturing research data
    """
    class Meta:
        model = DrinkSurvey
        fields = ['research_person','research_area', 'drink']
        exclude = ['research_id','researcher','added']
        widgets = {
            'research_person':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name',
                'required':'true',
            }),

            'research_area': forms.Select(attrs={
                'class': 'form-control',
                'required': 'true',
            }),

            'drink': forms.Select(attrs={
                'class': 'form-control',
                'required': 'true',
            })
        }
