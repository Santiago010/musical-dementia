"""form publications"""

# Django
from django.forms import ModelForm

# Models
from publications.models import Publication

# Utilities
import pdb

class NewPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['user','profile','image_front','image_back','description','tag_musical_genre','price','exchange','content']

