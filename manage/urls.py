from django.urls import path
from .import views


app_name = 'manage'
urlpatterns = [
   
    path('', views.IndexView.as_view(), name="index"),
    path('manage_top/', views.Managetopviews.View.as_view(), name="manage_top"),
    path('manage_toptable/', views.Managetoptableviews.View.as_view(), name="manage_toptable"),
    path('manage_searchresult/', views.Managesearchresultviews.View.as_view(), name="manage_searchresult"), 
]
