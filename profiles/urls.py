"""urls profiles"""

# Django
from django.conf.urls import url
from django.urls import path

# Views
from profiles import views

app_name='profiles'

urlpatterns = [
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='login/',
        view=views.login_user,
        name='login'
    ),
    path(
        route='signup/',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='update/',
        view=views.update_profile,
        name='update'
    ),
    path(
        route='<int:id>/',
        view=views.ProfileDetailView.as_view(),
        name='details'
    ),
]
