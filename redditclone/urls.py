from django.urls import include, path
from django.contrib import admin
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('', post_views.home, name='home'),
]
