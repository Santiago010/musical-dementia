"""musicaldementia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path,include

# Views app publications
from publications import views as views_publications

# View app profiles
from profiles import views as views_profiles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_publications.view_publications,name='publications'),
    path('/new',views_publications.view_new_publications,name='new_publications'),
    path('users/login/',views_profiles.login_user, name="login_user"),
    path('users/logout/',views_profiles.logout_view,name="logout_user"),
    path('users/signup/',views_profiles.signup_view,name='signup_user'),
    path('users/update/',views_profiles.update_profile,name="update_user")
]
