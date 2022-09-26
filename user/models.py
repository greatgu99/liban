from django.db import models

# Create your models here.
class User(models.Model):
    # 用户名
    userName = models.CharField(max_length=200)
    # 昵称
    nickName = models.CharField(max_length=200)
    # 密码
    password = models.CharField(max_length=200)
    # 学号
    userId = models.CharField(max_length=200)
    # 头像
    userImg = models.CharField(max_length=200,blank=True)
    # 院系
    userDepartment = models.CharField(max_length=200)
    # 权限
    authority = models.IntegerField()
    def __str__(self):
        return self.nickName