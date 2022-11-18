from django.urls import path
from .import views


app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search_advanced/', views.SearchAdvancedView.as_view(), name="search_advanced"),
    path('shop/<slug:category_slug>/', views.ProductListView.category_list, name='category_list'),
    path('product_list/', views.ProductListView.product_all, name="product_list"),
    path('product_all/', views.ProductAllView.as_view(), name="product_all"),
    path('item/<int:pk>-<slug:slug>', views.ProductDetailView.as_view(), name='detail'),
    path('search_result/', views.SearchResultsView.as_view(), name="search_result"),
    path('review/<int:pk>/', views.ReviewView.as_view(), name="review"), 
    path('review_edit/', views.ReviewEditView.as_view(), name="review_edit"), 
    path('review_delete/<int:pk>/', views.ReviewDeleteView.as_view(), name="review_delete"),
    # path('user_review_page/<int:pk>/', views.UserReviewPageView.as_view(), name="user_review_page"), 
    # path('wish_list/', views.WishListView.as_view(), name="wish_list"),
    # path('rank_list/', views.RankListView.as_view(), name="rank_list"),
    #path('like_for_post/', views.like_for_post, name="like_for_post"),
    path('item/', views.ItemView.as_view(), name="item"),
    # path('wish_delete/', views.WishDeleteView.as_view(), name="wish_delete"),
]