from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from shop.models import *
from project.models import *
from django.db.models import Q
import datetime
from django.shortcuts import render
import json


def top(request):
    # ページの閲覧数
    json_file = open('manage/json/summary.json', 'r')
    json_date = json.load(json_file)

    for date in json_date:
        if date["page_path"] == "/":
            top = date["page_views"]
        elif date["page_path"] == "/rank_list/":
            rank = date["page_views"]
        elif date["page_path"] == "/product_list/":
            product = date["page_views"]
        elif date["page_path"] == "/search_advanced/": # 今は検索画面
            word = date["page_views"]

    # 年齢割合
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

    # 渡す変数
    params = {
        'other' : other,
        'young' : young, 
        'adulthood' : adulthood,
        'senior' : senior,
        'top' : top,
        'rank' : rank,
        'product' : product,
        'word' : word,
    }

    return render(request, 'manage_top.html', params)
    
    
class ManageTableView(LoginRequiredMixin, generic.ListView):
    template_name = "manage_toptable.html"
    model = CustomUser
    paginate_by = 10

    def get_queryset(self):
        user_list = CustomUser.objects.order_by('-date_joined')

        for user in user_list:
            today = datetime.date.today()
            if user.user_birthday is None:
                None
            else:
                birthday = int(today.strftime("%Y%m%d")) - int(user.user_birthday.strftime("%Y%m%d"))
                age = birthday//10000
                user.user_birthday = age

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