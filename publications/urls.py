"""urls publications"""

# Django
from django.urls import path

# Views
from publications.views import view_new_publications, view_publications

app_name = "publications"

urlpatterns = [
    path(
        route='',
        view=view_publications,
        name='list'
    ),
    path(
        route='new/',
        view=view_new_publications,
        name='new'
    )
]



