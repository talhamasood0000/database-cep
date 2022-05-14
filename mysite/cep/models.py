from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class MyUser(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.user.username



class Guest(models.Model):
    name=models.ForeignKey(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Members(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    type=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name.user.username

class InternationalChapter(models.Model):
    yp_id=models.AutoField(primary_key=True)
    region_no=models.IntegerField()
    
class CoreBody(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    post=models.CharField(max_length=100,null=False)
    image_field=models.ImageField(upload_to='core_body/')
    duties=models.CharField(max_length=100,null=False)
    ypid=models.ForeignKey(InternationalChapter,on_delete=models.CASCADE)

    def __str__(self):
        return self.post

class ExecutiveMembers(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    image_field=models.ImageField(upload_to='executive_members/',null=True)

    def __str__(self):
        return self.user.name.user.username

class GeneralMember(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    duties=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.name.user.username

class Activities(models.Model):
    event_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    image_field=models.ImageField(upload_to='activities/',null=True)
    registration_fee=models.IntegerField()
    venue=models.CharField(max_length=100,null=False)
    date_time=models.DateTimeField(null=False)
    no_of_attendees=models.IntegerField()
    member_id=models.ForeignKey(ExecutiveMembers,on_delete=models.CASCADE)
    details=models.CharField(max_length=1000,null=True)

    def get_absolute_url(self):
        return reverse('activity_detail', args=[self.event_id])

class Inventory(models.Model):
    item_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=100,null=False)
    quantity=models.IntegerField()
    issue=models.DateTimeField(null=True,blank=True)
    type=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Manages(models.Model):
    item_id=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    int_mem_id=models.ForeignKey(CoreBody,on_delete=models.CASCADE)

class Team(models.Model):
    name=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=100,null=True)
    domain=models.IntegerField()
    no_of_members=models.IntegerField()
    member_id=models.ForeignKey(GeneralMember,on_delete=models.CASCADE)
    lead_by=models.ForeignKey(ExecutiveMembers,on_delete=models.CASCADE)
    event_id=models.ForeignKey(Activities,on_delete=models.CASCADE)

class PartOf(models.Model):
    member_id=models.ForeignKey(Members,on_delete=models.CASCADE)
    name=models.ForeignKey(Team,on_delete=models.CASCADE)

class Reports(models.Model):
    report_id=models.AutoField(primary_key=True)
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
    id=models.AutoField(primary_key=True)
    issue_date=models.DateTimeField(default=timezone.now)
    return_date=models.DateTimeField(null=False)
    item_id=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    int_mem_id=models.ForeignKey(Members,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_id.name)+" issued to "+str(self.int_mem_id.name.user.username)

class Contact(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=100,null=False)
    phonenumber=models.IntegerField(null=False)
    subject=models.CharField(max_length=100,null=False)
