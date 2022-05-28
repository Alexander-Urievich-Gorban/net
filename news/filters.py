import django_filters as filter
from django import forms
from .models import Post, PostLike, Profile
from .service import get_client_ip


class PostFilter(filter.FilterSet):
    CHOICES_RATING_DATE = (
        ('rating', 'По рейтингу'),
        ('crate_at', 'По дате'),
    )

    ordering_by_rating_date = filter.ChoiceFilter(label='', choices=CHOICES_RATING_DATE,
                                                  method='filter_ordering_by_rating_date')

    def filter_ordering_by_rating_date(self, queryset, name, value):
        sort = '-rating' if value == 'rating' else '-create_at'
        return queryset.order_by(sort)
