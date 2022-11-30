from django.urls import path
from .import views


app_name = 'manage'
urlpatterns = [
    path('top/', views.age, name="top"),
    path('table/', views.ManageTableView.as_view(), name="table"),
    path('search/', views.SearchView.as_view(), name="search"),
]
