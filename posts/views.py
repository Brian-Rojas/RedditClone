from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post
from django.utils import timezone

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
        return render(request, 'posts/create.html')
