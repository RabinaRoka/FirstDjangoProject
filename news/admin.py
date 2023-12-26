from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_desc','news_image')  #for showing title and description

admin.site.register(News, NewsAdmin) #after register you can see models in admin

# Register your models here.
