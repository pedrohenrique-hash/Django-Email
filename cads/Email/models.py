from django.db import models

class SendEmail(models.Model):
    
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    
class Register(models.Model):
    name = models.CharField(max_length=80)
    years = models.IntegerField()
    state = models.CharField(max_length=2)
    district = models.CharField(max_length=80)
    email = models.EmailField(max_length=200)


# Create your models here.
