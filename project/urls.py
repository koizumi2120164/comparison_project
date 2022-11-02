from django.urls import path
from .import views


app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('search-results/', views.SearchResultsView.as_view(), name="search_results"),
]
