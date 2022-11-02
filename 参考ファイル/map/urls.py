from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('storefront/', views.StorefrontView.as_view(), name="storefront"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('all/', views.MapListView.product_all, name='product_all'),
    path('item/<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('map/<slug:category_slug>/', views.MapListView.category_list, name='category_list'),
    path('scrape/', views.BeautifulSoupTest.as_view(), name="scrape"),

]