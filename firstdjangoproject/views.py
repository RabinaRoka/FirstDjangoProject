from django.core import paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForms     #importing function name defined in forms.py
from intro.models import intro
from news.models import News
from ContactInfo.models import contactinfo
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives

    #data = {         #passing data from django view to html
       # 'title':'Home',    #key of django dictionary
       # 'bodydata':'welcome to rabina first django project<3',
        #'clist':['PHP','Java','Django'],
        #'numbers':[10,20,30,40,50],
        #'studentDetails':[
          #  {'name':'Rabina','level':6},    #two dictionary 
           # {'name':'Sachin','level':5}
       # ]
    #}
def homepage(request):
    #for sending designed or hmtl content in mail
    Subject = 'Testing Mail'
    from_email = 'rokarabina113@gmail.com'
    msg = '<p> Hello<b> Welcome to Rabina World</b></p>'
    to = 'rabinaroka112@gmail.com'
    msg = EmailMultiAlternatives(Subject,msg,from_email,[to])
    msg.content_subtype = 'html'
    msg.send()

    ###for sending simple text in mail
    send_mail(
        "Testing Mail",
        "Here is the message.",
        "rokarabina113@gmail.com",
        ["rabinaroka112@gmail.com"],
        fail_silently=False,
    )
    if request.method=="GET":
       output=request.GET.get('output')
       
       newsData=News.objects.all();
    data={
      'newsData':newsData
    }
    return render(request,"index.html",data)
def newsDetails(request, slug):
    if request.method == "GET":
        st = request.GET.get('blogname', None)
        if st:
            newsDetails = News.objects.filter(news_title__icontains=st)
        else:
            # Retrieve all news items if no search criteria is provided
            newsDetails = News.objects.all()
    else:
        # If it's not a GET request, retrieve all news items
        newsDetails = News.objects.all()

      ##logic for using pagination
      #making variable and calling the function paginator
      #paginate through what details and how many data you want to show
    paginator=Paginator(newsDetails,2)
        #adding page number so, get page number
    page_number=request.GET.get('page')
        #in which page number you are or to show page number of showing data
    NewsDataFinal=paginator.get_page(page_number)
    #FOR LAST PAGE NUMBER
    totalpage=NewsDataFinal.paginator.num_pages
    #for 2 and 3 list comprehensive

    data = {
        'newsDetails':NewsDataFinal,
        'lastpage':totalpage,
        'totalPageList':[ n+1 for n in range(totalpage)]
    }
    return render(request, "newsDetails.html", data)

#YO CHAI LINK JE CLICK GARYOO TYO MATRA DETAILS AAUNA  YO GARDA FOR LOOP LAGAUNU PARDAINA TEMPLATE MA
#def newsDetails(request, newsid):
  #newsDetails = News.objects.get(id=newsid)  #for making dynamic data and dynamic url
  #st = request.GET.get('blogname', None)
  #if st!=None:
   #    newsDetails = News.objects.filter(news_title__icontains=st)
  #data={
    #'newsDetails':newsDetails
   #}
  #return render(request, "newsDetails.html",data)

def projects(request):          #making function for projects page
   #getting table data through objects.all()
   #ordering query in ascending or descending through order_by('')
   #[:2]using limits in query like selectquery through django syntax
   projectsData = intro.objects.all().order_by('intro_title')[:2] #bring all data
   #or a in projectsData:
     #print(a.intro_title)
   #print(projects)
   data={
     'projectsData':projectsData
   }

   return render(request, "projects.html",data)#return HttpResponse("<b>Welcome To My First Django Project</b>")



def intro(request):          #making function for projects page

   return render(request, "intro.html")#return HttpResponse("<b>Welcome To My First Django Project</b>")

def blog(request):       #making function for blog page

   return render(request, "blog.html")

def saveInfo(request):
  n=''
  if request.method=='POST':
    #getting data
    Name=request.POST.get('Name')
    Email=request.POST.get('Email')
    Phone_Number=request.POST.get('Phone_Number')
    Enquiry=request.POST.get('Enquiry')
    en=contactinfo(Name=Name,Email=Email,Phone_Number=Phone_Number,Enquiry=Enquiry)
#insert into db
    en.save()

    ###for sending mail we have to concatinate in en
   # send_mail(
        #"Testing Mail",
        #"Here is the message.",
        #"rokarabina113@gmail.com",
        #["rabinaroka112@gmail.com"],
        #fail_silently=False,
    #)
    n="Data Submitted Successfully"
  return render(request, "contact.html",{'n':n})

def contact(request):    #making function for contact page
   
   return render(request, "contact.html")

def marksheet(request):    #making function for marksheet page
  if request.method=="POST": #LOGIC FOR POST method and making variables
      s1=eval(request.POST.get('Subject1'))   #getting five subject data
      s3=eval(request.POST.get('Subject2'))   #getting five subject data
      s2=eval(request.POST.get('Subject3'))   #getting five subject data
      s4=eval(request.POST.get('Subject4'))   #getting five subject data
      s5=eval(request.POST.get('Subject5'))
      t=s1+s2+s3+s4+s5
      p=t*100/500;
      #for division
      if p>=60:
        d="First Division"
      elif p>=48:
        d="Second Division"
      elif p>=35:
        d="Third Division"
      else:
        d="fail"  
      data={         #making dictionary for fetching data in html page
        'total':t,
        'per':p,
        'div':d
      }
      return render(request, "marksheet.html",data)   #passing data and returning after if condition
  return render(request, "marksheet.html")   #rendering first page while opening page
def saveevenodd(request):
  c=''
  if request.method=="POST":   #Checking for method
    #for handling blank data using manual form validation
    if request.POST.get('num1')=="":
      return render(request, "evenodd.html",{'error':True})

    n=eval(request.POST.get('num1'))   #getting value with field value
    if n%2==0:
      c="Even Number"
    else:
      c="Odd Number"
  pass
  return render(request, "evenodd.html",{'c':c})

def calculator(request):    #making function for calculator page
 
  #for csrf token
  c=''   #Passing empty first
  try:   #error handling
   if request.method=="POST":
      n1=eval(request.POST.get('num1'))      #eval used to convert number, float
      n2=eval(request.POST.get('num2'))
      opr=request.POST.get('opr')    #getting same num1, num2, opr from the html input tag
      if opr=="+":
        c=n1+n2;
      elif opr=="-":
        c=n1-n2
      elif opr=="*":
        c=n1*n2
      elif opr=="/":
        c=n1/n2
      elif opr=="%":
        c=n1%n2

  except:        
    c="Invalid operation..."      #if text was send then this message occurs
    print(c)
  return render(request, "calculator.html", {'c':c}) 

def submitform(request):    #making function for contact page

 try:
   if request.method =="POST":        #Condition for post method
    n1=int(request.POST.get('num1'))  #passing through name and getting input
    n2=int(request.POST.get('num3'))
    result=n1+n2;   #sum of both input

    data={        #making dictionary for storing data
       'n1':n1,
       'n2':n2,
       'output':result
    }  
    return HttpResponse(result)
 except:
   pass
 
def UserForm(request):    #making function for contact page
 
 #use of GET method
 #for error handling use try and except
 result=0
 fn=userForms()  #making variable
 data={'form':fn}   #mking pair of key and value
 try:     

   ###GET method    
   #n1=request.GET['Num1']    #passing through name
   #n2=request.GET['Num2']
  #if request.method =="GET": or
   #n1=int(request.GET.get('num1'))  #passing through name and getting input
   #n2=int(request.GET.get('num3'))
   #result=n1+n2;   #sum of both input
  
  #POST Method
   if request.method =="POST":        #Condition for post method
    n1=int(request.POST.get('num1'))  #passing through name and getting input
    n2=int(request.POST.get('num3'))
    result=n1+n2;   #sum of both input

    data={        #making dictionary for storing data
       'n1':n1,
       'n2':n2,
       'output':result,
       'form':fn

    }
    
    url="/?output{}".format(result)  #with data #for redirect to another page

    return HttpResponseRedirect(url)   #for redirecting to other page
 except:
   pass
 return render(request, "UserForm.html", data)

def course(request):
    return HttpResponse("Hi, Here you can see your courses")

def courseDetails(request,courseid):   #for dynamic route
    return HttpResponse(courseid)