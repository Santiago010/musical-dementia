"""views profiles"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError

# Utilities
import pdb

# Form
from profiles.forms import UpdateDataForm, SignupForm

# Models
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your views here.



def login_user(request):
    if request.method == 'POST':
        data_user = {
            'username' : request.POST['username'],
            'password' : request.POST['password']
        }

        user = authenticate(
            request=request,
            username=data_user['username'],
            password = data_user['password']
        )

        if user:
            login(
                request=request,
                user=user
            )
            return redirect('publications')
        else : 
            return render(
                request=request,
                template_name='profiles/login.html',
                context={'error':'Nombre de usuario o contraseña incorrectos.'}
            )
    
    return render(
        request=request,
        template_name='profiles/login.html',
    )


@login_required
def logout_view(request):
    logout(request=request)
    return redirect('login_user')


def signup_view(request):
    if request.method == 'POST':
        form_signup = SignupForm(request.POST)

        if form_signup.is_valid():
            form_signup.save()
            return redirect('login_user')
        else:
            form_signup.add_error('password',ValidationError("La contraseña de confirmacion no concide."))

    else :
        form_signup = SignupForm()

    return render(
        request=request,
        template_name='profiles/signup.html',
        context={'form': form_signup}
    )
    
@login_required
def update_profile(request):
    current_profile = request.user.profile
    
    if request.method == 'POST':
        data_form = UpdateDataForm(request.POST,request.FILES)
        if data_form.is_valid():
            new_data = data_form.cleaned_data
            query_profile = Profile.objects.get(id=current_profile.id)
            query_profile.photo = new_data['photo']
            query_profile.interest = new_data['interest']
            query_profile.phone_number = new_data['phone_number']
            query_profile.save()
            return redirect('publications')


    else : 
        data_form = UpdateDataForm()

    
    return render(
        request=request,
        template_name='profiles/update.html',
        context= {'form':UpdateDataForm}
    )