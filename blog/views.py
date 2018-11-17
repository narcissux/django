import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post


# 首页
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'post_list': post_list})

# post详情
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions={
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    })
    return render(request, 'blog/detail.html',
                  context={'post': post})
