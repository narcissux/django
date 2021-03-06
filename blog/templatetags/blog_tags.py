from ..models import Post, Category
from django import template

register = template.Library()

#获取最近文章标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#获取归档标签
@register.simple_tag
def get_archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#获取文章分类标签
@register.simple_tag
def get_categorys():
    return Category.objects.all()



