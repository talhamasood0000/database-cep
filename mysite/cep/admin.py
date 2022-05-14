from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.MyUser)
admin.site.register(models.Guest)
admin.site.register(models.Members)
admin.site.register(models.InternationalChapter)
admin.site.register(models.CoreBody)
admin.site.register(models.ExecutiveMembers)
admin.site.register(models.GeneralMember)
admin.site.register(models.Activities)
admin.site.register(models.Inventory)
admin.site.register(models.Manages)
admin.site.register(models.Team)
admin.site.register(models.PartOf)
admin.site.register(models.Reports)
admin.site.register(models.Views)
admin.site.register(models.Supervises)
admin.site.register(models.RequestView)
admin.site.register(models.Contact)
