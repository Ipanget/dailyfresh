from django.db import models


class BaseManager(models.Manager):
    """抽象模型管理器基类"""
    def get_one_object(self, **filters):
        """根据条件进行查询"""
        try:
            obj = self.get(**filters)
        except self.model.DoesNotExist:
            obj = None
        return obj

    def create_one_object(self, **kwargs):
        """新增一个self所在模型类的数据"""
        # 1.获取self所在的模型类
        model_class = self.model
        # 2.创建一个model_class类对象
        obj = model_class(**kwargs)
        # 3.添加进数据库
        obj.save()
        # 4.返回obj
        return obj