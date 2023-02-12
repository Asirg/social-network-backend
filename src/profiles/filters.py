from django_filters import rest_framework as filters
from django.db.models import Q

from .models import (
    UserNet, 
    Follower,
    Technology,
)

class FollowerFilter(filters.FilterSet):
    class Meta:
        model = Follower
        fields = {
            'subscription': ['exact'],
            'follower': ['exact'],
            'relation': ['exact'],
        } 

class UserFilter(filters.FilterSet):

    search = filters.CharFilter(field_name='search', method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(username__icontains = value) |
            Q(first_name__icontains = value) |
            Q(middle_name__icontains = value) |
            Q(last_name__icontains = value)
        )

    class Meta:
        model = UserNet
        fields = ['search']

class TechnologyFilter(filters.FilterSet):
    class Meta:
        model = Technology
        fields = {
            'name': ['icontains']
        }