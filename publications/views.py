"""views publications"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError

# Utilities
import pdb

# Form
from publications.form import NewPublicationForm

# Models
from publications.models import Publication

# Create your views here.


@login_required
def view_publications(request):
    list_publications = Publication.objects.all().order_by("-publication_date")
    return render(
        request=request,
        template_name='publications/list.html',
        context={
            'publications': list_publications
        }
    )

@login_required
def view_new_publications(request):
    if request.method == 'POST':
        form_new_publications = NewPublicationForm(request.POST,request.FILES)

        if form_new_publications.is_valid():
            form_new_publications.save()
            return redirect('publications')

    else:
        form_new_publications = NewPublicationForm()


    return render(
        request=request,
        template_name='publications/new.html',
        context={
            'user' : request.user.pk,
            'profile' : request.user.profile.pk,
            'form': form_new_publications
        }
    )