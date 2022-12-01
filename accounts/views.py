from django.shortcuts import render

# Create your views here.
def account(request):

    if  request.user.is_staff:
        return redirect('top/' )
   

