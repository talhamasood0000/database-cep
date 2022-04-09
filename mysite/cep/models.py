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

class Members(models.Model):
    name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    type=models.CharField(max_length=100,null=False)

class InternationalChapter(models.Model):
    yp_id=models.IntegerField(primary_key=True)
    region_no=models.IntegerField()

class CoreBody(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    post=models.CharField(max_length=100,null=False)
    duties=models.CharField(max_length=100,null=False)
    ypid=models.ForeignKey(InternationalChapter,on_delete=models.CASCADE)

class ExecutiveMembers(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)




class GeneralMember(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    duties=models.CharField(max_length=100,null=True)


class Activities(models.Model):
    event_id=models.IntegerField(primary_key=True)
    registration_fee=models.IntegerField()
    venue=models.CharField(max_length=100,null=False)
    date_time=models.DateTimeField(null=False)
    no_of_attendees=models.IntegerField()
    member_id=models.ForeignKey(ExecutiveMembers,on_delete=models.CASCADE)

class Inventory(models.Model):
    item_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=100,null=False)
    quantity=models.IntegerField()
    issue=models.DateTimeField(null=False)
    type=models.CharField(max_length=100,null=False)

class Manages(models.Model):
    item_id=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    int_mem_id=models.ForeignKey(CoreBody,on_delete=models.CASCADE)

class Team(models.Model):
    name=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=100,null=True)
    domain=models.IntegerField()
    no_of_members=models.IntegerField()
    member_id=models.ForeignKey(GeneralMember,on_delete=models.CASCADE)
    event_id=models.ForeignKey(Activities,on_delete=models.CASCADE)


class PartOf(models.Model):
    member_id=models.ForeignKey(Members,on_delete=models.CASCADE)
    name=models.ForeignKey(Team,on_delete=models.CASCADE)

class Reports(models.Model):
    report_id=models.IntegerField(primary_key=True)
    no_of_attendees=models.IntegerField()
    proceedings=models.CharField(max_length=100,null=False)
    event_id=models.ForeignKey(Activities,on_delete=models.CASCADE)

class Views(models.Model):
    report_id=models.ForeignKey(Reports,on_delete=models.CASCADE)
    international_member=models.ForeignKey(CoreBody,on_delete=models.CASCADE)

class Supervises(models.Model):
    report_id=models.ForeignKey(Activities,on_delete=models.CASCADE)
    international_member=models.ForeignKey(CoreBody,on_delete=models.CASCADE)


class RequestView(models.Model):
    request_date=models.CharField(max_length=100,null=False,primary_key=True)
    issue_date=models.DateTimeField(null=False)
    return_date=models.DateTimeField(null=False)
    item_id=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    int_mem_id=models.ForeignKey(Members,on_delete=models.CASCADE)

