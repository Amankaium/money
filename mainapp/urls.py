from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from write import views as write_views

urlpatterns = [

    path('', write_views.write, name='homepage'),

    path('login/', auth_views.login,
        {'template_name': 'main/login.html'},
        name='login'),

    path('logout/', auth_views.logout,
        {'next_page': '/'},
        name='logout'),
]
