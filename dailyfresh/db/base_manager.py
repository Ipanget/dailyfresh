from django.db import models
import copy


class BaseManager(models.Manager):
    """抽象模型管理器基类"""
    def get_all_valid_fields(self):
        """获取self所在模型类的有效属性列表"""
        # 获取self所在的模型类
        model_class = self.model
        # 获取model_class这个模型类有效属性的元组
        attr_str_list = []
        attr_tuple = model_class._meta.get_fields()
        for attr in attr_tuple:
            #  使用 isinstance() 判断attr是否是models.Foreignkey这个类型
            if isinstance(attr, models.ForeignKey):
                attr_name = '%s_id' % attr.name
            else:
                attr_name = attr.name
            attr_str_list.append(attr_name)
        return attr_str_list

    def get_one_object(self, **filters):
        """根据条件进行查询"""
        try:
            obj = self.get(**filters)
        except self.model.DoesNotExist:
            obj = None
        return obj

    def create_one_object(self, **kwargs):
        """新增一个self所在模型类的数据"""
        # 获取self.mode这个类有效属性列表
        valid_fields = self.get_all_valid_fields()
        # 拷贝kwargs
        kws = copy.copy(kwargs)
        # 去除kwargs中的无效参数
        for key in kws:
            if key not in valid_fields:
                # 去除无效参数
                kwargs.pop(key)
        # 1.获取self所在的模型类
        model_class = self.model
        # 2.创建一个model_class类对象
        obj = model_class(**kwargs)
        # 3.添加进数据库
        obj.save()
        # 4.返回obj
        return obj

    def get_object_list(self, filters={}, order_by=('-pk', )):
        """按照filters中的条件查询数据，并进行排序"""
        object_list = self.filter(**filters).order_by(*order_by)
        return object_list
