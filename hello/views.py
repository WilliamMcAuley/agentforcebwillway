from django.shortcuts import render
# import os
# from django.http import HttpResponse

# from .models import Greeting,Account
from .models import Account

# Create your views here.

def index(request):
     return render(request,"index.html")

def db(request):
     accounts = Account.objects.all()

     return render(request, "db.html", {"accounts": accounts})

