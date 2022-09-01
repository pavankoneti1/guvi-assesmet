from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DataBase(models.Model):
    user = models.EmailField( blank=False, null=True, name='user')
    first = models.CharField( max_length=20, blank=False, null=True, name='first')
    last = models.CharField( max_length=20, blank=False, null=True, name='last')
    # email = models.EmailField(blank=False, null=False, name='email')
    contact = models.IntegerField(max_length=10, blank=True, null=True, name='contact')
    dob = models.DateField(name='dob')
    age = models.IntegerField( null=True,name='age')
    password = models.CharField(null=False, blank=True, name='password', max_length=25)

