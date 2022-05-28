from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [

    path("", views.PostListView.as_view(), name="post_list"),
    path("post_create/", views.CreatePostView.as_view(), name="post_create"),
    path("add_favorite/", views.AddFavoriteView.as_view(), name="add_favorite"),
    path("remove_favorite/", views.RemoveFavorite.as_view(), name="remove_favorite"),
    path("like/", views.LikeView.as_view(), name="like"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),

]
