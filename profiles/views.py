"""views profiles"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Utilities
import pdb

# Form
from profiles.forms import UpdateDataForm

# Models
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your views here.



def login_user(request):

    # pdb.set_trace()
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
                context={'error':'usuario invalido'}
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
        data_user = {
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'username' : request.POST['username'],
            'password' : request.POST['password'],
            'password_confirmation' : request.POST['password_confirmation'],
            'email' : request.POST['email']

        }
        
        if data_user['password'] != data_user['password_confirmation']:
            return render(request=request,template_name='profiles/signup.html',context={'error':'las contraseñas no conciden'})
        
        data_user.pop('password_confirmation')
        new_user = User.objects.create_user(**data_user)
        new_profile = Profile(user=new_user)
        new_profile.save()
        return redirect('login_user')

    return render(
        request=request,
        template_name='profiles/signup.html'
    )
    
@login_required
def update_profile(request):
    current_profile = request.user.profile
    

    # print(current_profile.id)
    if request.method == 'POST':
        data_form = UpdateDataForm(request.POST,request.FILES)
        if data_form.is_valid():
            new_data = data_form.cleaned_data
            query_profile = Profile.objects.filter(id=current_profile.id)
            print(query_profile)


    else : 
        data_form = UpdateDataForm()

    
    return render(
        request=request,
        template_name='profiles/update.html',
        context= {'form':UpdateDataForm}
    )