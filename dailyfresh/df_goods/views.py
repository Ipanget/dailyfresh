from django.shortcuts import render
from df_goods.models import Goods, Image
from df_goods.enums import *
from django.core.paginator import Paginator  # 导入分页类
# Create your views here.

# http://127.0.0.1:8000


def home_list_page(request):
    """显示首页"""

    # 查询水果的四个商品和三个新品
    fruits = Goods.objects.get_goods_by_type(goods_type_id=FRUIT, limit=4)
    fruits_new = Goods.objects.get_goods_by_type(goods_type_id=FRUIT, limit=3, sort='new')
    seafood = Goods.objects.get_goods_by_type(goods_type_id=SEAFOOD, limit=4)
    seafood_new = Goods.objects.get_goods_by_type(goods_type_id=SEAFOOD, limit=3, sort='new')
    meat = Goods.objects.get_goods_by_type(goods_type_id=MEAT, limit=4)
    meat_new = Goods.objects.get_goods_by_type(goods_type_id=MEAT, limit=3, sort='new')
    eggs = Goods.objects.get_goods_by_type(goods_type_id=EGGS, limit=4)
    eggs_new = Goods.objects.get_goods_by_type(goods_type_id=EGGS, limit=3, sort='new')
    vegetables = Goods.objects.get_goods_by_type(goods_type_id=VEGETABLES, limit=4)
    vegetables_new = Goods.objects.get_goods_by_type(goods_type_id=VEGETABLES, limit=3, sort='new')
    frozen = Goods.objects.get_goods_by_type(goods_type_id=FROZEN, limit=4)
    frozen_new = Goods.objects.get_goods_by_type(goods_type_id=FROZEN, limit=3, sort='new')

    #  组织上下文数据
    context = {
        'fruits': fruits, 'fruits_new': fruits_new,
        'seafood': seafood, 'seafood_new': seafood_new, 'meat': meat,
        'meat_new': meat_new, 'eggs': eggs, 'eggs_new': eggs_new, 'vegetables': vegetables,
        'vegetables_new': vegetables_new, 'frozen': frozen, 'frozen_new': frozen_new,

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


def goods_list(request, goods_type_id, pindex):
    """显示商品列表页面"""
    # 获取排序方式
    sort = request.GET.get('sort', 'default')
    # 根据goods_t_id查询商品信息
    goods_li = Goods.objects.get_goods_by_type(goods_type_id=goods_type_id, sort=sort)
    # 根据商品类型查询新品信息
    goods_new = Goods.objects.get_goods_by_type(goods_type_id=goods_type_id, sort='new', limit=2)

    # 进行分页操作
    paginator = Paginator(goods_li, 1)
    # 获取第pindex页的内容
    pindex = int(pindex)
    # 返回值是一个page对象
    goods_li = paginator.page(pindex)

    # 获取分页后的总页数
    nums_pages = paginator.num_pages
    # 控制页码列表
    if nums_pages < 5:
        pages = range(1, nums_pages + 1)
    elif pindex <= 3:
        pages = range(1, 6)
    elif nums_pages - pindex < 2:
        pages = range(nums_pages-4, nums_pages + 1)
    else:
        pages = range(pindex-2, pindex+3)

    # 定义上下文
    context = {'goods_new': goods_new, 'goods_li': goods_li,
               'type_id': goods_type_id, 'sort': sort, 'pages': pages, 'type_title': GOODS_TYPE[int(goods_type_id)]}

    # 使用模板文件
    return render(request, 'df_goods/list.html', context)






































