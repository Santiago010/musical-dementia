"""models profile"""

# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/photos', null=True, blank=True)
    sales_or_changes = models.BigIntegerField(default=0,null=True)
    phone_number = models.IntegerField(null=True, blank=True)
    interest = models.TextField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
