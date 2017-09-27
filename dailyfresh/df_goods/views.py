from django.shortcuts import render
from df_goods.models import Goods, Image
from df_goods.enums import *

# Create your views here.


def home_list_page(request):
    """显示首页"""

    # 查询水果的四个商品和三个新品
    fruits = Goods.objects.get_goods_by_type(goods_type_id=FRUIT, limit=4)
    fruits_new = Goods.objects.get_goods_by_type(goods_type_id=FRUIT, limit=3, sort='new')
    seafood = Goods.objects.get_goods_by_type(goods_type_id=SEAFOOD, limit=4)
    seafood_new = Goods.objects.get_goods_by_type(goods_type_id=SEAFOOD, limit=3, sort='new')

    #  组织上下文数据
    context = {
        'fruits': fruits, 'fruits_new': fruits_new,
        'seafood': seafood, 'seafood_new': seafood_new
    }
    return render(request, 'df_goods/index.html', context)


def goods_detail(request, goods_id):
    """显示商品详情页面"""
    # # 根据商品id查询商品信息
    # goods = Goods.objects.get_goods_by_id(goods_id=goods_id)
    # # 获取商品的详情图片
    # images = Image.objects.get_image_by_goods_id(goods_id=goods_id)
    # goods =Goods.objects.get_goods_by_id_with_image(goods_id=goods_id)

    goods = Goods.objects_logic.get_goods_by_id(goods_id=goods_id)
    #  根据商品类型查询新品信息
    goods_new = Goods.objects.get_goods_by_type(goods_type_id=goods.goods_type_id, limit=2, sort='new')

    # 使用模板文件
    context = {'goods': goods, 'goods_new': goods_new}
    return render(request, 'df_goods/detail.html', context)