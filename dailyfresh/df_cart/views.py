from django.shortcuts import render
from django.http import JsonResponse
from utils.decorators import login_required
from df_cart.models import Cart

# Create your views here.

# /card/add/


# @login_required
def cart_add(request):
    """添加商品到购物车"""
    # 1,获取商品ID和商品数目
    goods_id = request.GET.get('goods_id')
    goods_count = request.GET.get('goods_count')
    passport_id = request.session['passport_id']
    print(goods_id)
    print(passport_id)
    # 2,添加商品到购物车
    res = Cart.objects.add_one_cart_info(passport_id=passport_id, goods_id=goods_id, goods_count=int(goods_count))
    # 3,判断返回json数据
    if res:
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

