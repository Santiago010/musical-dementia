"""models profiles"""

# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/photos', null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    interest = models.TextField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.interest
    