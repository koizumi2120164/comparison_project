from django.urls import path
from .import views
from comparison_project import settings_common, settings_dev
from django.contrib.staticfiles.urls import static

app_name = 'project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('word_detail/<int:pk>/', views.WordDetailView.as_view(), name="word_detail"),
    path('word_update/<int:pk>/', views.WordUpdateView.as_view(), name="word_update"),
    path('word_delete/<int:pk>/', views.WordDeleteView.as_view(), name="word_delete"),
    path('wordpost_create', views.WordCreateView.as_view(), name="wordpost_create"),
    path('wordreiew_list', views.WordReiewListView.as_view(), name="wordreiew_list"),
    path('search_advanced/', views.SearchAdvancedView.as_view(), name="search_advanced"),
    path('shop/<slug:category_slug>/', views.ProductListView.category_list, name='category_list'),
    path('product_list/', views.ProductListView.product_all, name="product_list"),
    path('item/<int:pk>-<slug:slug>', views.ProductDetailView.as_view(), name='detail'),
    path('search_result/', views.SearchResultsView.as_view(), name="search_result"),
    path('review/<int:pk>/', views.ReviewView.as_view(), name="review"),
    path('review_create', views.ReviewCreateView.as_view(), name="review_create"),
    path('review_edit/<int:pk>/', views.ReviewEditView.as_view(), name="review_edit"), 
    path('review_delete/<int:pk>/', views.ReviewDeleteView.as_view(), name="review_delete"),
    path('user_review_page/<int:pk>/', views.UserReviewPageView.as_view(), name="user_review_page"),
    path('review_list/<int:pk>/', views.ReviewListView.as_view(), name="review_list"),
    path('word_list/<int:pk>/', views.WordListView.as_view(), name="word_list"),                                                                     
    path('wish_list/<int:pk>/', views.WishListView.as_view(), name="wish_list"),
    path('recently_view/<int:pk>/', views.RecentlyViewedView.as_view(), name="recently_view"),
    path('rank_list/', views.RankListView.as_view(), name="rank_list"),
    #path('like_for_post/', views.like_for_post, name="like_for_post"),
    path('item/', views.ItemView.as_view(), name="item"),
    # path('wish_delete/', views.WishDeleteView.as_view(), name="wish_delete"),
    path('profile_edit/<int:pk>/', views.ProfileEditView.as_view(), name="profile_edit"),
    path('profile_update/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile_update"),
    path('word_wish/<int:pk>/', views.wish_word, name="word_wish"),
    path('remove_word_wish/<int:pk>/', views.remove_wish_word, name="remove_word_wish"),
]

if settings_dev.DEBUG:
    urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)