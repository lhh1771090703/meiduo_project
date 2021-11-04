from django.db import models

# Create your models here.

# 1自己定义模型
# class User(models.Model):
#     username=models.CharField(max_length=20,unique=True)
#     password=models.CharField(max_length=20)
#     mobile=models.CharField(max_length=11,unique=True)

# 2站在巨人的肩膀上面,使用系统自带的模型
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# 因为没有mobile字段,所以使用继承AbstractUser来增加mobile字段
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    class Meta:
        db_table='tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name

