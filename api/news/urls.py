from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='list_post'),
    path('post', views.PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('favorites', views.FavoriteListView.as_view()),
    path('liked', views.LikedPostView.as_view()),
    path('your_value/post/<int:pk>', views.PostLikeView.as_view({
        'put': 'update'
    })),
    path('favorites/add/<int:pk>', views.PostAddFavoriteView.as_view({
        'put': 'update'
    })),
    path('favorites/remove/<int:pk>', views.PostRemoveFavoriteView.as_view({
        'put': 'update'
    }))
]
