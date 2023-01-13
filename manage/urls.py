from django.urls import path
from .import views


app_name = 'manage'
urlpatterns = [
    path('top/', views.top, name="top"),
    path('table/', views.ManageTableView.as_view(), name="table"),
    path('search_age/', views.AgeView.as_view(), name="age"),
    path('search_gender/', views.GenderView.as_view(), name="gender"),
    path('search_address/', views.AddressView.as_view(), name="address"),
]
