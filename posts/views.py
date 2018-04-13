from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post
from django.utils import timezone
from django.http import HttpResponse

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
        else:
            return render(
                request,
                'posts/create.html',
                {'error': 'Both fields are required'}
            )
        return render(request, 'posts/home.html')
    else:
        return render(request, 'posts/create.html')


def home(request):
    return render(request, 'posts/home.html')
