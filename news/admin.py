from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Post, PostLike, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "article")
    list_filter = ("article", "title", "author")
    search_fields = ("title", "author")
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("title", "trans_title", "article"),)
        }),
        (None, {
            "fields": (("content",), ("preview", "get_image"))
        }),
        (None, {
            "fields": (("author", "short_description"),)
        }),
        ("Options", {
            "fields": (("rating", "views"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'id')
    list_filter = ("post__article", "post__title", "ip")
    search_fields = ("post__title", "ip")


admin.site.register(Profile)
