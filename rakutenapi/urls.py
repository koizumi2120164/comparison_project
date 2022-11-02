from django.urls import path

from . import views

app_name = 'rakutenapi'
urlpatterns = [
    path('rakutenapi/', views.IndexView.as_view(), name="index"),
]