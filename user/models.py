from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileModel(models.Model):
    GENDER_CHOICES = (
        ('M',"Male"),
        ('F',"Female"),
        ('other',"NotSpecified")
        )
    user = models.OneToOneField(User,on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    address = models.TextField(max_length=200)
    phone_no = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to="images/profile/picture/",blank=True,null=True,default='default/dummy-profile-pic.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"