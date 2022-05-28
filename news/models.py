from django.db.models import Sum, Avg

from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.utils import timezone


def day_diff(from_date, to_date):
    """Расчет времени жизни поста в часах"""
    diff = from_date - to_date
    days_in_between = diff.seconds / 60 / 60
    return days_in_between


def directory_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.__class__.__name__, instance.title[0], filename)


class Post(models.Model):
    article = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    trans_title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    short_description = models.TextField(max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.BigIntegerField(default=0)
    rating = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    preview = models.ImageField(upload_to=directory_path, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.id})

    def get_rating(self):
        """(лайки-дизлайки)+(просмотры/время жизни поста)"""
        try:
            a = self.like.all().aggregate(Sum("value"))['value__sum'] + 1 - 1
        except:
            a = 0
        try:
            b = self.views / day_diff(timezone.now(), self.create_at)
        except:
            b = self.views
        self.rating = float("%.1f" % (a + b))
        self.save()


class PostLike(models.Model):
    """Оценки постов"""
    ip = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.post.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Post, blank=True, related_name='profile')

    def __str__(self):
        return self.user.username
