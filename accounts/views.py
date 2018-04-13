from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # Before we check password check if username is unique
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(
                    request,
                    'accounts/signup.html',
                    {'error': "Username is already taken."}
                )
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                login(request, user)
        else:
            return render(
                request,
                'accounts/signup.html',
                {'error': "Password's didn't match."}
            )

        return HttpResponse('You signed up, woohoo!')
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return HttpResponse('You loged in as {}, welcome!!'.format(user.username))
        else:
            return render(request, 'accounts/login.html', {'error':'login failed'})
    else:
        return render(request, 'accounts/login.html')
