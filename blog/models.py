from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post (models.Model):

    #文章标题
    title = models.CharField(max_length=70)

    #文章内容
    body = models.TextField()

    #创作时间
    created_time = models.DateTimeField()

    #修改时间
    modefied_time = models.DateTimeField()

    #分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #标签
    tag = models.ManyToManyField(Tag, blank=True)

    #作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #对象toString
    def __str__(self):
        return self.title

    #文章地址
    #自定义 get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})





