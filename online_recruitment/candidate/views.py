from django.shortcuts import render
from .models import*

# Create your views here.
def landingpage(request):
    joblist = Job.objects.all()
    categories = Category.objects.all()
    context = {
        'job':[ ],
        'categories':[]
    }
    for job in joblist:
        temp = {
            'name': job.name,
            'place': job.place,
            'type': job.type,
            'salary': job.salary,
        }
        context['jobs'].append(temp)

    for category in categories:
        temp ={
            'name' : category.name
        }
        context['categories'].append(temp)

    return render(request, "landingpage.html") 

def notFoundPage(request):
    return render(request, "404.html") 

def aboutPage(request):
    return render(request, "about.html") 

def categoryPage(request):
    return render(request, "category.html") 

def contactpage(request):
    return render(request, "contact.html")

def jobdetailpage(request):
    return render(request,"job-detail.html")

def joblistpage(request):
    joblist = Job.objects.all()
    context = {
        'jobs': [ ]
    }
    for job in joblist:
        temp = {
            'name': job.name,
            'place': job.place,
            'type': job.type,
            'salary': job.salary,
        }
        context['jobs'].append(temp)

    return render(request,"job-list.html")

def testimonial(request):
    return render(request,"testimonial.html")

def resume_upload(request):
    return render(request,"resume_upload.html")

def registrationform(request):
    if request.method =='POST':
        print('post recieved')
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        gender = request.POST.get('gender')

        print(name, email, url, gender)
    return render(request ,'registration_form.html')

def dashboardpage(request):
    return render(request,"dashboard.html")