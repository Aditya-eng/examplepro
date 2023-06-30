from django.shortcuts import render
from django.http import HttpResponse
# import random

def index(request):
     my_dict = {"insert_me":"yo what u say feeling good i am feeling great tired of this fucking hate;lfkjsdf;ljs views.py"}
     return render(request,'exampleapp/index.html',context=my_dict)

def math_screenshot_file(request):
     # math_dict = {""}
     return render(request,'exampleapp/math_screenshot_file.html',context=None)


def steve(request):
     return render(request,"exampleapp/steve_jobs_vid.html")
# Create your views here.
