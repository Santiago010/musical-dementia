"""search tags views"""

# Django
import publications
import profiles
from django.shortcuts import render

# Models
from profiles.models import Profile
from publications.models import Publication


# Utilities
import pdb

# Create your views here.

def principal(request):
    return render(
        request=request,
        template_name='search_tags/principal.html',
        context={}
    )

def search_tags_for_profiles(request):
    if request.method == 'POST':
        if not request.POST['tag']:
            return render(
                request=request,
                template_name='search_tags/search_profiles.html',
                context={'error':'debes ingresar un genero'}
            )
        else:
            profiles_tag = Profile.objects.filter(interest__contains=request.POST['tag'])
            return render(
                request=request,
                template_name='search_tags/search_profiles.html',
                context={'tag':request.POST['tag'],'profiles': profiles_tag}
            )

    return render(
        request=request,
        template_name='search_tags/search_profiles.html',
        context={}
    )
    
def search_tags_for_publications(request):
    if request.method == 'POST':
        if not request.POST['tag']:
            return render(
                request=request,
                template_name='search_tags/search_publications.html',
                context={'error': 'debes ingresar un genero'}
            )
        else :
            publications_tag = Publication.objects.filter(tag_musical_genre__contains=request.POST['tag'])
            return render(
                request=request,
                template_name='search_tags/search_publications.html',
                context={'tag':request.POST['tag'],'publications': publications_tag}
            )

    return render(
        request=request,
        template_name='search_tags/search_publications.html',
        context={}
    )
