from django.contrib import admin

# Register your models here.
from .models import MyUser,Guest,Members,InternationalChapter,CoreBody,ExecutiveMembers,GeneralMember,Activities,Inventory,Manages

admin.site.register(MyUser)
admin.site.register(Guest)
admin.site.register(Members)
admin.site.register(InternationalChapter)
admin.site.register(CoreBody)
admin.site.register(ExecutiveMembers)
admin.site.register(GeneralMember)
admin.site.register(Activities)
admin.site.register(Inventory)
admin.site.register(Manages)