import logging
import requests
import urllib.request

from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages


from map.models import Product, Category
from .forms import InquiryForm

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

class StorefrontView(generic.TemplateView):
    template_name = "store.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('map:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class MapListView(generic.ListView):
    model = Product, Category
    
    def categories(request):
        return {
            'categories': Category.objects.all()
        }

    def product_all(request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})

    def category_list(request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'category': category, 'products':products})

class ProductDetailView(generic.DetailView):
    template_name = 'detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    success_url = reverse_lazy('map:product_all')
    
class BeautifulSoupTest(generic.TemplateView):
    template_name = "scrapetest.html"
    def index(request):
        # 対象サイトのURL
        url = "https://www.amazon.co.jp/dp/B09Z91T4K4"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "Accept-Language": "ja",
        }

        r = requests.get(url, headers=headers)

        # スクレイピング
        soup = BeautifulSoup(r.text, "lxml")
        # 全てのaタグを抽出
        name = soup.select_one(selector="#productTitle").getText()
        name = name.strip()

        price = soup.select_one(selector="#priceblock_ourprice").getText()
        price = float(price[1:])

        # テンプレートに渡すデータを格納 
        context = {
            'name': name,
            'price': price,
        }

        return render(request, 'scrapetest.html', context)