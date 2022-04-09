from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class InternationalChapter(models.Model):
    yp_id=models.IntegerField(primary_key=True)
    region_no=models.IntegerField(max_length=3)
    


