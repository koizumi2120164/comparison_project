from django.urls import path
from .import views


app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="shop:wordreview_list"),
    path('shop:worddetail/', views.SearchView.as_view(), name="shop:worddetail"),
    path('shop:wordpost/', views.SearchResultsView.as_view(), name="shop:wordpost"),
]
