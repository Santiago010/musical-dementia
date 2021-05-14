"""urls publications"""

# Django
from django.urls import path

# Views
from publications import views

app_name = "publications"

urlpatterns = [
    path(
        route='',
        view=views.view_publications,
        name='list'
    ),
    path(
        route='new/',
        view=views.view_new_publications,
        name='new'
    ),
    path(
        route='<int:id>/',
        view=views.view_edit_publications,
        name='edit'
    ),
    path(
        route='delete/<int:id>/',
        view=views.view_delete_publications,
        name='delete'
    ),
    path(
        route='change_state/<int:id>/',
        view=views.view_change_state,
        name='change_state'
    )
]



