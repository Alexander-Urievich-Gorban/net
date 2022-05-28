from rest_framework.filters import OrderingFilter
from rest_framework import permissions, generics
from rest_framework.parsers import MultiPartParser, FormParser
from .classes import CreateRetrieveUpdateDestroy, Update
from .permissions import IsAuthor
from news.models import Post, PostLike, Profile
from news.service import get_client_ip, post_query
from .serializers import ListPostSerializer, PostSerializer, PostLikeSerializer, PostFavoriteSerializer
from .pagination import CustomPageNumberPagination


class FavoriteListView(generics.ListAPIView):
    """Список избранных постов
    """
    pagination_class = CustomPageNumberPagination
    serializer_class = ListPostSerializer
    filter_backends = [OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['views', 'rating', 'create_at']

    def get_queryset(self):
        return post_query(self.request).filter(in_favorite=True)


class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD поста
    """
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def get_queryset(self):
        return post_query(self.request)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_object(self):
        self.object = super().get_object()
        self.object.views += 1
        self.object.save()
        return self.object


class LikedPostView(generics.ListAPIView):
    """Список лайкнутых постов"""
    serializer_class = ListPostSerializer
    pagination_class = CustomPageNumberPagination
    ordering_fields = ['views', 'rating', 'create_at']
    filter_backends = [OrderingFilter]

    def get_queryset(self):
        return post_query(self.request).filter(your_value=1)


class PostListView(generics.ListAPIView):
    """Список всех постов"""
    pagination_class = CustomPageNumberPagination
    serializer_class = ListPostSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['views', 'rating', 'create_at']

    def get_queryset(self):
        return post_query(self.request)


class PostLikeView(Update):
    """Редактирование списка лайкнутых постов"""
    serializer_class = PostLikeSerializer
    permission_classes_by_action = {
        'update': [permissions.AllowAny],
    }

    def get_queryset(self):
        return post_query(self.request)

    def get_object(self):
        self.object = super().get_object()
        return PostLike.objects.get(post_id=self.object.id, ip=get_client_ip(self.request))


class PostAddFavoriteView(Update):
    """Добавление поста в спискок избранных"""
    serializer_class = PostFavoriteSerializer
    permission_classes_by_action = {'update': [permissions.IsAuthenticated]}

    def perform_update(self, serializer):
        try:
            self.request.user.profile.favorites.add(self.get_object())
        except:
            pass

    def get_queryset(self):
        return post_query(self.request)


class PostRemoveFavoriteView(Update):
    """Удаление поста из списка избранных"""
    serializer_class = PostFavoriteSerializer
    permission_classes_by_action = {'update': [permissions.IsAuthenticated]}

    def perform_update(self, serializer):
        try:
            self.request.user.profile.favorites.remove(self.get_object())
        except:
            pass

    def get_queryset(self):
        return post_query(self.request)
