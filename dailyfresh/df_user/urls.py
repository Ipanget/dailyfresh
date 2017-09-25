from django.conf.urls import url
from df_user import views

urlpatterns = [
    #  显示注册页面
    url(r'^register/$', views.register),
    # 用户注册
    url(r'^register_handle/$', views.register_handle),
    #  校验用户名是否存在
    url(r'^check_user_exist/$', views.check_user_exist),


    #  显示登录页面
    url(r'^login/$', views.login),
    # 用户登录校验
    url(r'^login_check/$', views.login_check),
    # 用户退出登录
    url(r'logout/$', views.logout),

    # 显示用户
    url(r'^$', views.user),
    #  显示用户收货地址
    url(r'^address/$', views.address),
    # 显示用户订单
    url(r'^order/$', views.order),


]