from django.urls import path
from .import views


app_name = 'manage'
urlpatterns = [
    path('top/', views.ManageTopView.as_view(), name="top"),
    path('table/', views.ManageTableView.as_view(), name="table"),
    path('search/', views.SearchView.as_view(), name="search"),
]
