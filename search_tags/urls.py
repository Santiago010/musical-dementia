"""urls search_tags"""

# Django
from django.urls import path

# Views
from search_tags.views import principal, search_tags_for_profiles, search_tags_for_publications

app_name = "search_tags"

urlpatterns = [
    path(
        route='',
        view=principal,
        name='principal'
    ),
    path(
        route='profiles/',
        view=search_tags_for_profiles,
        name='profiles',
    ),
    path(
        route='publications/',
        view=search_tags_for_publications,
        name='publications'
    )
]


