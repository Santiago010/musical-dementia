"""forms profiles"""

from django import forms

class UpdateDataForm(forms.Form):
    photo = forms.ImageField(label='Foto de perfil: ')
    phone_number = forms.IntegerField(label='numero de telefono: ',widget=forms.NumberInput(),min_value=7)
    interest = forms.CharField(label='Escribe tus intereses musicales: ',widget=forms.Textarea(),max_length=255, min_length=10)