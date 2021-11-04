from django.urls import converters

# 定义转换器,需要注册转换器
class UsernameConverters:
    regex = '[a-zA-Z0-9_-]{5,20}'
    def to_python(self,value):
        return value