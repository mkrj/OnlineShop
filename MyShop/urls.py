"""MyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.views.static import serve

from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchViewSet, BannerViewSet, IndexCategoryViewSet
from MyShop.settings import MEDIA_ROOT

router = DefaultRouter()

# 配置 goods 的 url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置 category 的 url
router.register(r'categories', CategoryViewSet, base_name='categories')

router.register(r'hotsearchs', HotSearchViewSet, base_name='hotsearchs')

# 轮播图 url
router.register(r'banners', BannerViewSet, base_name='banners')

# 首页商品谢列数据
router.register(r'indexgoods', IndexCategoryViewSet, base_name='indexgoods')


urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^', include(router.urls))
]
