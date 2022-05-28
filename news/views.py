from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import View
from .filters import PostFilter
from .forms import PostForm
from .models import Post, PostLike, Profile
from .service import get_client_ip, post_query


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=post_query(self.request))
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return PostFilter(self.request.GET, queryset=post_query(self.request)).qs.filter(
                Q(title=search) | Q(trans_title=search))
        liked = self.request.GET.get('liked')
        if liked:
            return PostFilter(self.request.GET, queryset=post_query(self.request).filter(your_value=1)).qs
        favorite = self.request.GET.get('favorite')
        if favorite:
            return PostFilter(self.request.GET,
                              queryset=post_query(self.request).filter(in_favorite=True)).qs
        return PostFilter(self.request.GET, queryset=post_query(self.request)).qs


class AddFavoriteView(View):
    def post(self, request):
        Profile.objects.get(id=request.POST.get('user')).favorites.add(Post.objects.get(id=request.POST.get('post')))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RemoveFavorite(View):
    def post(self, request):
        Profile.objects.get(id=request.POST.get('user')).favorites.remove(Post.objects.get(id=request.POST.get('post')))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class LikeView(View):
    """Получение лайков или дизлайков и запись их в бд"""

    def post(self, request):
        try:
            obj = PostLike.objects.get(ip=get_client_ip(request), post_id=request.POST.get('post'))
            if int(obj.value) == int(
                    request.POST.get('value')):
                obj.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                obj.delete()
                PostLike.objects.update_or_create(
                    ip=get_client_ip(request),
                    post_id=request.POST.get('post'),
                    value=int(request.POST.get('value'))
                )
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except:
            PostLike.objects.update_or_create(
                ip=get_client_ip(request),
                post_id=request.POST.get('post'),
                value=int(request.POST.get('value'))
            )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CreatePostView(CreateView):
    """Создание поста"""
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return post_query(self.request)
