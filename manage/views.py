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

    # 各変数名
    dates = CustomUser.objects.order_by('-date_joined')
    young = 0
    adulthood = 0
    senior = 0
    day = 0

    man = 0
    woman = 0
    gender = 0

    kanto = 0
    kansai = 0
    other = 0
    address = 0


    for date in dates:
        # 年齢割合
        today = datetime.date.today()

        if date.user_birthday is None:
            day += 1

        else:
            age = int(today.strftime("%Y%m%d")) - int(date.user_birthday.strftime("%Y%m%d"))
            age2 = age//10000

            if age2 <= 18:
                young += 1
            elif age2 >= 60:
                senior += 1
            else:
                adulthood += 1

        # 性別割合
        if date.user_gender is None:
            gender += 1

        else:
            if date.user_gender == "男性":
                man += 1
            else:
                woman += 1

        # 地域割合
        if date.user_address is None:
            address += 1

        else:
            if date.user_address == "関東":
                kanto += 1
            elif date.user_address == "関西":
                kansai += 1
            else:
                other += 1

        

    # 渡す変数
    params = {
        'day' : day, 'young' : young, 'adulthood' : adulthood,'senior' : senior,
        'top' : top, 'rank' : rank, 'product' : product, 'word' : word,
        'man' : man, 'woman' : woman, 'gender' : gender,
        'kanto' : kanto,'kansai' : kansai,'other' : other,'address' : address,
    }

    return render(request, 'manage_top.html', params)
    
    
class ManageTableView(LoginRequiredMixin, generic.ListView):
    template_name = "manage_toptable.html"
    model = CustomUser
    paginate_by = 10

    def get_queryset(request):
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
    

class AgeView(generic.TemplateView):
    template_name = "manage_age.html"
    model = Product
    paginate_by = 10
    wish = []

    def get_queryset(self, request):
        keyword = request.GET.get("keyword")
        products = Product.objects.filter(Q(product_name__contains=keyword))

        for product in products:
            wish = Wishlist.objects.filter(wished_item=product.productID)
            user = CustomUser.objects.filter(username=wish.userID)

        # 各変数名
        young = 0
        adulthood = 0
        senior = 0
        day = 0

        for date in user:
            # 年齢割合
            today = datetime.date.today()

            if date.user_birthday is None:
                day += 1

            else:
                age = int(today.strftime("%Y%m%d")) - int(date.user_birthday.strftime("%Y%m%d"))
                age2 = age//10000

                if age2 <= 18:
                    young += 1
                elif age2 >= 60:
                    senior += 1
                else:
                    adulthood += 1

            all = day + young + adulthood + senior
            name = product.product_name

            # 渡す変数
            params = {
                'name' : name, 'day' : day, 'young' : young, 'adulthood' : adulthood, 'senior' : senior, 'all' : all
            }

            return render(request, 'manage_age.html', params), user


class GenderView(generic.TemplateView):
    template_name = "manage_gender.html"
    model = Product
    paginate_by = 10
    wish = []

    def get_queryset(self, request):
        keyword = request.GET.get("keyword")
        products = Product.objects.filter(Q(product_name__contains=keyword))

        for product in products:
            wish = Wishlist.objects.filter(wished_item=product.productID)
            user = CustomUser.objects.filter(username=wish.userID)

        # 各変数名
        gender = 0
        man = 0
        woman = 0

        for date in user:
            # 性別割合
            if date.user_gender is None:
                gender += 1

            else:
                if date.user_gender == "男性":
                    man += 1
                else:
                    woman += 1

        all = gender + man + woman
        name = product.product_name

        # 渡す変数
        params = {
            'name' : name, 'gender' : gender, 'man' : man, 'woman' : woman, 'all' : all
        }

        return render(request, 'manage_gender.html', params), user

class AddressView(generic.TemplateView):
    template_name = "manage_address.html"
    model = Product
    paginate_by = 10
    wish = []

    def get_queryset(self, request):
        keyword = request.GET.get("keyword")
        products = Product.objects.filter(Q(product_name__contains=keyword))

        for product in products:
            wish = Wishlist.objects.filter(wished_item=product.productID)
            user = CustomUser.objects.filter(username=wish.userID)

        # 各変数名
        address = 0
        kanto = 0
        kansai = 0
        other = 0

        for date in user:
            # 地域割合
            if date.user_address is None:
                address += 1

            else:
                if date.user_address == "関東":
                    kanto += 1
                elif date.user_address == "関西":
                    kansai += 1
                else:
                    other += 1

        all = kansai + kanto + other + address
        name = product.product_name

        # 渡す変数
        params = {
            'name' : name, 'address' : address, 'kanto' : kanto, 'kansai' : kansai, 'other' : other, 'all' : all
        }

        return render(request, 'manage_address.html', params),user
