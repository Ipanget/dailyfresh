from django.conf.urls import url
from df_goods import views

urlpatterns = [
    # 显示首页
    url(r'^$', views.home_list_page),

    # 商品详情显示
    url(r'^goods/(?P<goods_id>\d+)/$', views.goods_detail),

    # 商品列表
    url(r'^list/(?P<goods_type_id>\d+)/(?P<pindex>\d+)/$', views.goods_list),




]