from email import message
from re import M
from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=500)
    reply = models.TextField(max_length=1000, default='no-reply')
    is_replied=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)


    def __str__(self)->str:
        return f"{self.name} {self.subject}"