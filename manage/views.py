from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from shop.models import *
from project.models import *
from django.db.models import Q
import datetime
from django.shortcuts import render


class ManageTopView(LoginRequiredMixin, generic.TemplateView):
    template_name = "manage_top.html"
    model = CustomUser

    def age(request):
        days = CustomUser.objects.order_by('-date_joined')
        young = 0
        adulthood = 0
        senior = 0
        other = 0

        for day in days:
            today = datetime.date.today()
            birthday = datetime.date(day.user_birthday)
            age = int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))

            if age <= 18:
                young += 1
            elif age >= 60:
                senior += 1
            elif 18 > age > 60:
                adulthood += 1
            else:
                other += 1

        params = { 
            'other': other,
            'young': young,
            'adulthood' : adulthood,
            'senior' : senior,
        }

        return render(request, 'manage_top.html', params)



    
class ManageTableView(LoginRequiredMixin, generic.TemplateView):
    template_name = "manage_toptable.html"
    model = CustomUser
    paginate_by = 10

    def get_queryset(self):
        account = CustomUser.objects.order_by('-date_joined')
        return account
    

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






