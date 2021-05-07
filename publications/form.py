"""form publications"""

# Django
from django import forms

# Models
from publications.models import Publication

# Utilities
import pdb

class NewPublicationForm(forms.Form):
    image_front = forms.ImageField(required=True)
    image_back = forms.ImageField(required=True)
    description = forms.CharField(required=True)
    tag_musical_genre = forms.CharField(required=True, )
    price = forms.CharField(required=True)
    exchange = forms.BooleanField(required=False)
    content = forms.CharField(required=True)

    def clean(self):
        data = super().clean()
        image_front = data.get('image_front')
        image_back = data.get('image_back')

        if image_front == image_back:
            raise forms.ValidationError("Las imagenes de portada y contraportada no pueden ser las mismas")
        return data

    def save(self):
        data_new_publication = self.cleaned_data
        new_publication = Publication.objects.create(**data_new_publication)
        
        
