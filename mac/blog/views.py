from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'blog/index.html')

