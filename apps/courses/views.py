from django.shortcuts import render
from .models import Courses

# Create your views here.
def courses(request):
    cource = Courses.objects.all()

    context = {
        "cource" : cource
    }
    return render(request, "courses.html", context)


def detail_courses(request,id):
    cource= Courses.objects.get(id=id)


    context = {
        'cource':cource
    }


    return render(request,'single-course.html',context)

