from django.db import models

# Create your models here.
class BooksInfo(models.Model):
    book_name=models.CharField(max_length=10,unique=True,default='')
    pub_data=models.DateField(max_length=20)
    describle=models.TextField(max_length=100,default='')
    class Meta:
        # 改变数据库表名
        db_table='bookinfo'
        # 改变模型名
        verbose_name='用户管理'
