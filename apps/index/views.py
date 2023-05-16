from django.shortcuts import render
from .models import Settings
from apps.courses.models import Courses


# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    cource = Courses.objects.all()
    context ={
        'settings':settings,
        "cource" : cource

    }
    return render(request,'index.html',context)