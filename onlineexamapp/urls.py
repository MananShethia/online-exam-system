from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.support, name='support'),
    path('', views.about, name='about'),
    path('', views.blog, name='blog'),
    path('', views.contact, name='contact'),
]