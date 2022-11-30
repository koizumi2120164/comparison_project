from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from shop.models import *
from project.models import *
from django.db.models import Q
import datetime
from django.shortcuts import render


def age(request):
    days = CustomUser.objects.order_by('-date_joined')
    young = 0
    adulthood = 0
    senior = 0
    other = 0

    for day in days:
        today = datetime.date.today()

        if day.user_birthday is None:
            other += 1

        else:
            age = int(today.strftime("%Y%m%d")) - int(day.user_birthday.strftime("%Y%m%d"))
            age2 = age//10000

            if age2 <= 18:
                young += 1
            elif age2 >= 60:
                senior += 1
            else:
                adulthood += 1

    params = {
        'other' : other,
        'young' : young, 
        'adulthood' : adulthood,
        'senior' : senior
    }

    return render(request, 'manage_top.html', params)
    
    
class ManageTableView(LoginRequiredMixin, generic.ListView):
    template_name = "manage_toptable.html"
    model = CustomUser
    paginate_by = 10

    def get_queryset(self):
        user_list = CustomUser.objects.order_by('-date_joined')
        return user_list
    

class SearchView(generic.TemplateView):
    template_name = "manage_searchresult.html"
    model = Product
    paginate_by = 10

    def get_queryset(self, request):
        keyword = request.GET.get("keyword")
        product = Product.objects.filter(Q(product_name__contains=keyword))
        wish = Wishlist.objects.filter(wished_item=product.productID)
        user = CustomUser.objects.filter(username=wish.userID)
        return user


class Managetoptableview(generic.TemplateView):
    template_name = "manage_toptable.html"