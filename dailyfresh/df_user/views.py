from django.shortcuts import render, redirect
from df_user.models import Passport
from django.http import JsonResponse
from .models import *
from django.views.decorators.http import require_GET, require_POST, require_http_methods

# 导入任务函数
from df_user.tasks import send_register_success_mail


# 导入发送邮件函数
from django.core.mail import send_mail

from django.conf import settings

import time
# Create your views here.
#  register(登记簿)


def register(requset):
    '''显示注册页面'''
    return render(requset, 'df_user/register.html')


def register_handle(request):
    '''用户信息注册'''
    #  1、接收用户注册信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    #  2、将用户信息保存进数据库
    Passport.objects.add_one_passport(username=username, password=password, email=email)

    # 3、给客户发邮件
    # message = '<h1>欢迎您成为天天生鲜注册会员</h1>请记好您的注册信息:<br/>用户名:' + username + '<br/>密码:' + password
    # send_mail('欢迎信息', '', settings.EMAIL_FROM, [email], html_message=message)
    # 将任务函数放入任务队列
    send_register_success_mail.delay(username=username, password=password, email=email)
    #  4、跳转到登录页面
    return redirect('/user/login/')

@require_GET
def check_user_exist(request):
    """校验用户名对否存在"""
    #  1、获取用户名
    username = request.GET.get('username')
    #  2、获取用户名查询账户信息 get_one_passport(username)
    passport = Passport.objects.get_one_passport(username=username)
    print(username, passport)
    #  3、如果查到，返回json {'res':0} 查不到返回json{'res'：1}
    if passport:
        #  用户存在
        return JsonResponse({'res': 0})
    else:
        #  用户名可以用
        return JsonResponse({'res': 1})


def login(request):
    """返回登录页面"""
    return render(request, 'df_user/login.html')


@require_POST
def login_check(request):
    """用户登录校验"""
    # 1.接收用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    #  2,根据用户名和密码查找账户信息
    passport = Passport.objects.get_one_passport(username=username, password=password)
    if passport:
        # 用户名密码正确
        jres = JsonResponse({'res': 1})
        #  判断是否需要记住用户名
        remember = request.POST.get('remember')
        if remember == 'true':
            #  记住用户名
            jres.set_cookie('username', username, max_age=14*24*3600)
        return jres
    else:
        #  用户名或密码错误
        return JsonResponse({'res': 0})



def index(request):
    """首页"""
    return render(request, 'df_user/index.html')









