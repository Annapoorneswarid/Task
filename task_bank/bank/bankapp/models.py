from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='service')

    def __str__(self):
        return self.name

class Form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    account_type=models.CharField(max_length=250)


    def __str__(self):
        return self.name
