from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def user_information(request):
    print(request.user.is_superuser),
    if not request.user.is_superuser:
     return render(request,'manage/top')  
   

