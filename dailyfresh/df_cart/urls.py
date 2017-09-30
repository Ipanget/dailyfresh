from django.conf.urls import url
from df_cart import views
urlpatterns = [
    url(r'^add/$', views.cart_add),  # 添加商品到购物车
  ]
