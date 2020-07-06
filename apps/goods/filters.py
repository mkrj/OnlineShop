import django_filters
from django.db.models import Q


from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(field_name='shop_price', help_text='最低价格', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', help_text='最高价格', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter', label='类别')

    def top_category_filter(self, queryset, field_name, value):
        return queryset.filter(Q(category_id=value) |
                               Q(category__parent_category_id=value) |
                               Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'is_hot', 'is_new']
