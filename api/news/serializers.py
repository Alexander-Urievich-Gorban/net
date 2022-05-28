from rest_framework import serializers
from news.models import Post, PostLike, Profile


class PostSerializer(serializers.ModelSerializer):
    """ Вывод и редактирование поста
    """

    author = serializers.ReadOnlyField(source='author.username')
    dislikes_count = serializers.CharField(read_only=True)
    likes_count = serializers.CharField(read_only=True)
    your_value = serializers.IntegerField(read_only=True)
    views = serializers.CharField(read_only=True)
    rating = serializers.CharField(read_only=True)
    in_favorite = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class ListPostSerializer(serializers.ModelSerializer):
    """ Список постов
    """
    author = serializers.ReadOnlyField(source='author.username')
    dislikes_count = serializers.CharField(read_only=True)
    likes_count = serializers.CharField(read_only=True)
    your_value = serializers.IntegerField(default=0)
    in_favorite = serializers.BooleanField(default=False)

    class Meta:
        model = Post
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    """Редактирование лайк/дизлайк/0"""
    value = serializers.IntegerField(max_value=1, min_value=-1)

    class Meta:
        model = PostLike
        fields = ('value',)


class PostFavoriteSerializer(serializers.ModelSerializer):
    """удаляемый/добавляемый пост в избранное"""
    title = serializers.ReadOnlyField()
    trans_title = serializers.ReadOnlyField()
    preview = serializers.ImageField(read_only=True)
    content = serializers.ReadOnlyField()
    short_description = serializers.ReadOnlyField()
    article = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.username')
    dislikes_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    your_value = serializers.ReadOnlyField()
    views = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
