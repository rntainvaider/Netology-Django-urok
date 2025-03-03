from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter, CharFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    status = CharFilter(field_name="status")

    class Meta:
        model = Advertisement
        fields = ["created_at", "status"]
