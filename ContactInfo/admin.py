from django.contrib import admin
from ContactInfo.models import contactinfo

class ContactAdmin(admin.ModelAdmin):
    list_disp=('Name','Email','Phone_Number','Enqiry',)  #for showing title and description
#register model
admin.site.register( contactinfo, ContactAdmin) #after register you can see models in admin

