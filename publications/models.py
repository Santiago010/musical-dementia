"""models publications"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User
from profiles.models import Profile


# Create your models here.

class Publication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image_front = models.ImageField(upload_to='publications/images/front')
    image_back = models.ImageField(upload_to='publications/images/back')
    description = models.TextField()
    tag_musical_genre = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    exchange = models.BooleanField(default=False)
    content = models.TextField(default="Contenido no especificado")
    publication_date = models.DateField(auto_now_add=True)
