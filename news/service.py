from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import Post


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def data_query(request):
    return Post.objects.all().prefetch_related("like", "profile").annotate(
        likes_count=models.Count("like",
                                 filter=models.Q(like__value=1))
    ).annotate(
        dislikes_count=models.Count("like",
                                    filter=models.Q(like__value=-1))).annotate(
        your_value=Coalesce(Sum("like__value", filter=models.Q(like__ip=get_client_ip(request))), 0))


def post_query(request):
    """Формирование оптимизированного queryset"""
    try:
        return data_query(request).annotate(
        in_favorite=models.Count("profile", filter=models.Q(profile=request.user.profile)))
    except:
        return data_query(request)
