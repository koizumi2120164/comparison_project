from django.urls import path
from .import views


app_name = 'bbs'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('post_detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'), 
    path('like_for_post', views.like_for_post, name='like_for_post'),
]