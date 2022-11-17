from django.urls import path
from .import views


app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search_advanced/', views.SearchAdvancedView.as_view(), name="search_advanced"),
    # path('search_result/', views.SearchResultsView.as_view(), name="search_result"),
    # path('review/<int:pk>', views.ReviewView.as_view(), name="review"), 
    # path('review_edit/', views.ReviewEditView.as_view(), name="review_edit"), 
    # path('review_delete/', views.ReviewDeleteView.as_view(), name="review_delete"),
    # path('user_review_page/', views.UserReviewPageView.as_view(), name="user_review_page"), 
    path('shop/<slug:category_slug>/', views.ProductListView.category_list, name='category_list'),
    path('product_all/', views.ProductListView.product_all, name="product_all"),
    path('item/<int:pk>-<slug:slug>', views.ProductDetailView.as_view(), name='detail'),
]