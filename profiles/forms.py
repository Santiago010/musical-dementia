"""forms profiles"""

# Django
from django import forms

# Models
from profiles.models import Profile
from django.contrib.auth.models import User

import pdb

class SignupForm(forms.Form):
    username = forms.CharField(min_length=3,max_length=40,required=True)
    email = forms.EmailField(min_length=13, required=True)
    password = forms.CharField(min_length=8,required=True)
    password_confirmation = forms.CharField(min_length=8,required=True)
    first_name = forms.CharField(min_length=3,max_length=40,required=True)
    last_name = forms.CharField(min_length=3,max_length=40,required=True)


    def clean_username(self):
        current_username = self.cleaned_data["username"]
        verify_user_existence = User.objects.filter(username=current_username)
        if verify_user_existence:
            raise forms.ValidationError("El usuario ingresado ya existe.")
        return current_username
       
        

    def clean(self):
        data = super().clean()
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError("La contraseña de confirmacion no concide.")
        return data

    def save(self):
        data_new_user = self.cleaned_data
        data_new_user.pop('password_confirmation')

        new_user = User.objects.create_user(**data_new_user)
        new_profile = Profile.objects.create(user=new_user)



class UpdateDataForm(forms.Form):
    photo = forms.ImageField(required=True)
    phone_number = forms.IntegerField(min_value=7,required=True)
    interest = forms.CharField(min_length=10,required=True,max_length=255)