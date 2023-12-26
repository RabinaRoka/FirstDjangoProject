"""
URL configuration for firstdjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstdjangoproject import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [                           #making url for pages
    path('admin-panel/', admin.site.urls),
    path('', views.homepage, name='home'),   #using name attributes for URL tags
    path('projects/', views.projects),
    path('intro/', views.intro),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('form/', views.UserForm),
    path('newsDetails/<slug>', views.newsDetails),
    path('calculator/', views.calculator),
    path('marksheet/', views.marksheet),
    path('evenodd/', views.saveevenodd),     #give name attributes if you use any actions
    path('submitform/', views.submitform, name="submitform"),      #function name after views
    path('saveinfo/', views.saveInfo, name="saveinfo"),      #function name after views
    path('course/<courseid>', views.courseDetails),  #for dynamic route datatype(int,str,slug) should be clear
]
 #settings for file uploadation
if settings.DEBUG:  #Checking debug
    #calling two roots 
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
