from django.urls import path
from .import views


app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search_advanced/', views.SearchAdvancedView.as_view(), name="search-advanced"),
    path('search_result/', views.SearchResultsView.as_view(), name="search-result"),
    path('review_edit/', views.ReviewEditView.as_view(), name="review-edit"), 
]
