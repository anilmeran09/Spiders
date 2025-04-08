from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    # return HttpResponse("Hello world")
    return render(request,'index.html')

def get_data(request):
    return HttpResponse("Hello World.")

