"""admin profiles"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from profiles.models import Profiles

#Register your models here.

@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','interest')

class ProfileInline(admin.StackedInline):
    model = Profiles
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)