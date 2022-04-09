from ast import Mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from numpy import tri


# Create your models here.

class MyUser(models.Model):
    id=models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=20,null=True)


class Guest(models.Model):
    name=models.ForeignKey(MyUser,on_delete=models.CASCADE)

class Memebers(models.Model):
    name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    type=models.CharField(max_length=100,null=False)

class InternationalChapter(models.Model):
    yp_id=models.IntegerField(primary_key=True)
    region_no=models.IntegerField(max_length=3)

class CoreBody(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(Memebers,on_delete=models.CASCADE)
    post=models.CharField(max_length=100,null=False)
    duties=models.CharField(max_length=100,null=False)
    ypid=models.ForeignKey(InternationalChapter,on_delete=models.CASCADE)

class ExecutiveMembers(models.Model):
    user=models.ForeignKey(Memebers,on_delete=models.CASCADE)

class PartOf(models.Model):
    pass

class Team(models.Model):
    name=models.ForeignKey(Memebers,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,null=True)
    domain=models.IntegerField(max_length=1)
    no_of_members=models.IntegerField(max_length=3)


class GeneralMember(models.Model):
    user=models.ForeignKey(Memebers,on_delete=models.CASCADE)
    duties=models.CharField(max_length=100,null=True)




