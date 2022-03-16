from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.support, name='support'),
    path('', views.about, name='about'),
    path('', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
