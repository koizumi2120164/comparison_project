from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_superuser:
     return render(request,'manage/manage_top.html')  
   

