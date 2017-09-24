from django.db import models
#  导入模型基类
from db.base_model import BaseModel
#  导入散列值函数
from utils.get_hash import get_hash
import hashlib

# Create your models here.


class PassportManager(models.Manager):
    #  账户模型管理器类
    def add_one_passport(self, username, password, email):
        #  添加一个用户注册信息
        #  1、获取self所在模型
        model_class = self.model
        #   2、创建一个model_class模型类对象
        obj = model_class(username=username, password=get_hash(password), email=email)
        #  3、保存进数据库
        obj.save()
        # 4、返回
        return obj

    def get_one_passport(self, username, password=None):
        """根据用户名查询账户信息"""
        if password is None:
            # 获取到用户名查找信息
            obj = self.filter(username=username).exists()
        else:
            # 根据用户名和密码查找账户信息
            obj = self.filter(username=username, password=get_hash(password)).exists()
            print(obj)
        return obj
            # exist（存在）

    def is_exist(self, username):
        # 判断用户是否已存在
        if self.model.objects.filter(username=username).exists():
            #  存在
            return self.model()
        else:
            #  不存在
            return None

    def check_username_password(self, username, password):
        """校验用户名和密码是否都正确"""
        print('username')
        if self.model.objects.filter(username=username, password=password).exists():
            return True
        else:
            return False


class Passport(BaseModel):
    #  账户信息模型类
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱地址')

    #  自定义模型管理器类对象
    objects = PassportManager()

    class Meta:
        #  account(账户)
        db_table = 's_user_account'



