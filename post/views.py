from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def postPage(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'post/post.html',context)

def detailPage(request, slug):
    post = get_list_or_404(Post, slug=slug)

    context = {
        "post":post
    }
    return render(request, 'post/detail.html', context)

