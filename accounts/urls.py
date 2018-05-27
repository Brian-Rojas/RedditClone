from django.urls import path
from . import views as accView

app_name = 'accounts'

urlpatterns = [
    path('signup/', accView.signup, name='signup'),
    path('login/', accView.login, name='login'),
    path('logout/', accView.logoutView, name='logout'),
]
