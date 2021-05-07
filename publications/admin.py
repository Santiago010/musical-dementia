"""admin profiles"""

# Django
from django.contrib import admin

# Models
from publications.models import Publication

# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('user','publication_date','description','tag_musical_genre','price','exchange',)
    list_filter = ('tag_musical_genre','exchange',)