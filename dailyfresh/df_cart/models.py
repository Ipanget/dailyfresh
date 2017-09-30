from django.db import models

from db.base_manager import BaseManager

from db.base_model import BaseModel

from df_goods.models import Goods

# Create your models here.


class CartManager(BaseManager):
    """购物车模型管理器类"""
    # 获取购物车信息
    def get_one_cart_info(self, passport_id, goods_id, ):
        """判断用是否添加过此商品"""
        print('CartManager get_cart_count')
        cart_info = self.get_one_object(passport=passport_id, goods=goods_id)
        return cart_info

    """添加商品到购物车"""
    def add_one_cart_info(self, passport_id, goods_id, goods_count):
        print('CartManager add_one_cart-1')
        cart_info = self.get_one_cart_info(passport_id=passport_id, goods_id=goods_id)
        print('CartManager add_one_cart-2')
        goods = Goods.objects.get_goods_by_id(goods_id=goods_id)
        print('CartManager add_one_cart-3')
        if cart_info:
            print('CartManager add_one_cart-4')
            # 1.如果用户购物车中添加过该商品,更新商品数量
            total_count = cart_info.goods_count + goods_count
            # 判断商品库存
            print(total_count)
            print(goods.goods_stock)
            if total_count <= goods.goods_stock:
                # 库存充足
                cart_info.goods_count = total_count
                cart_info.save()
                return True
            else:
                # 库存不足
                return False
        else:

            # 如果客户购物车中没有添加过该商品,创新记录
            # 判断商品库存
            print(goods.stock)
            if goods_count <= goods.goods_stock:
                # 库存不足
                print('CartManager add_one_cart-5')
                print(passport_id)
                self.create_one_object(passport_id=passport_id, goods_id=goods_id, goods_count=goods_count)
                print('CartManager add_one_cart-6')
                return True
            else:
                # 库存不足
                return False


class Cart(BaseModel):
    """购物车模型类"""
    passport = models.ForeignKey('df_user.Passport', verbose_name='账户')
    goods = models.ForeignKey('df_goods.Goods', verbose_name='商品')
    goods_count = models.IntegerField(default=1, verbose_name='商品总数')

    objects = CartManager()

    class Meta:
        db_table = 's_cart'



