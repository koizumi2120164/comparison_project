from django.urls import path
from .import views


app_name = 'manage'
urlpatterns = [
   
    path('', views.IndexView.as_view(), name="index"),
    path('manage_top/', managetopviews.View.as_view(), name=""),
]
