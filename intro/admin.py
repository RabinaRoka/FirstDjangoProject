from django.contrib import admin
from intro.models import intro
class introAdmin(admin.ModelAdmin):  #inherit model and admin.Modeladmin give permission to display field
    list_display=('intro_title','intro_desc')  #For Displaying field in admin page
# Register your models here.
admin.site.register(intro,introAdmin)
