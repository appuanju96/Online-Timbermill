
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your models here.

class mill(models.Model):
    muname = models.CharField(max_length=100)
    mill_name=models.CharField(max_length=100)
    mill_loc=models.CharField(max_length=100)
    mob=models.BigIntegerField()
    email=models.CharField(max_length=100)

class User1(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mob=models.BigIntegerField()
    loc=models.CharField(max_length=100)
class sell(models.Model):
    
    user=models.CharField(max_length=100)
    usname=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    m_name=models.CharField(max_length=100)
    wood_id=models.CharField(max_length=100)
    type_of_wood=models.CharField(max_length=100)
    length=models.CharField(max_length=100)     
    width=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class usell(models.Model):
    mill=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    umail=models.CharField(max_length=100)
    wood=models.CharField(max_length=100)
    length=models.IntegerField()
    width=models.IntegerField()
    rate=models.IntegerField()
    status=models.CharField(max_length=100)

class timber(models.Model):
    cno=models.BigIntegerField()
    month=models.CharField(max_length=100)
    year=models.IntegerField()
    cvv=models.CharField(max_length=3)
    status=models.CharField(max_length=100)
class bank(models.Model):
    amt=models.FloatField() 
    status=models.CharField(max_length=100)
class bkdetails(models.Model):
    wo_id=models.CharField(max_length=50)
    user=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    mill=models.CharField(max_length=100)
    memail=models.CharField(max_length=100)
    timber=models.CharField(max_length=100)
    leng=models.CharField(max_length=100)
    cirf=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    svdate=models.DateField(auto_now_add=False)
    svtime=models.TextField()    
class usdetails(models.Model):
    user=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    mill=models.CharField(max_length=100)
    memail=models.CharField(max_length=100)
    timber=models.CharField(max_length=100)
    leng=models.CharField(max_length=100)
    cirf=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    svdate=models.DateField(auto_now_add=False)
    svtime=models.TextField() 
