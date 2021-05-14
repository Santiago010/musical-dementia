"""views publications"""

# Django
from profiles.models import Profile
import publications
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.urls import reverse

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
            return redirect('publications:list')

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


@login_required
def view_edit_publications(request,id):
    edit_publication = Publication.objects.get(id=id)
    return render(request=request,template_name='publications/edit.html',context={'publication':edit_publication})

@login_required
def view_delete_publications(request,id):
    publication_delete = Publication.objects.get(id=id)
    publication_delete.delete()
    url_redirect = reverse('users:details', kwargs={'id':request.user.profile.id})
    return redirect(url_redirect)

@login_required
def view_change_state(request,id):
    profile_publication = Profile.objects.get(id=id)
    profile_publication.sales_or_changes = profile_publication.sales_or_changes + 1 
    pdb.set_trace()
    url_redirect = reverse('users:details', kwargs={'id':request.user.profile.id})
    return redirect(url_redirect)