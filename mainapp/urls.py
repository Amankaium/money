from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from write import views as write_views

urlpatterns = [

    path('', views.home, name='home'),

    path('login/', auth_views.login,
        {'template_name': 'main/login.html'},
        name='login'),

    path('logout/', auth_views.logout,
        {'next_page': '/'},
        name='logout'),

    path('sign-up', views.sign_up, name='sign-up'),
]
