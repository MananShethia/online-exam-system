from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.support, name='support'),
    path('', views.about, name='about'),
    path('', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('studentSignup/', views.studentSignup, name='studentSignup'),
    path('facultySignup/', views.facultySignup, name='facultySignup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('studentList/', views.studentList, name='studentList'),
    path('ajax/studentApprove/', views.studentApprove, name='studentApprove'),

    path('addCourse/', views.addCourse, name='addCourse'),
]
