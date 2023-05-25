from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Team

def teamPage(request):
    post = Team.objects.all()
    context = {
        'post': post
    }
    return render(request, 'team/team.html', context)

def detailPage(request, slug):
    post = get_list_or_404(Team, slug=slug)
    context = {
        "post":post
    }
    return render(request, 'team/detail.html', context)

