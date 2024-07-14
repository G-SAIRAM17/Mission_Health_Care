from django.urls import path
from .import views

urlpatterns=[
    #-----------signup urls----------------------------
    path('',views.psignup,name='psignup'),
    path('dsignup',views.dsignup,name='dsignup'),
    path('rsignup',views.rsignup,name='rsignup'),
    #-----------login urls----------------------------
    path('plogin/',views.plogin,name='plogin'),
    path('dlogin/',views.dlogin,name='dlogin'),
    path('rlogin/',views.rlogin,name='rlogin'),
    #-----------dashboard urls----------------------------
    path('pdashboard/',views.pdashboard,name='pdashboard'),
    path('dbashboard/',views.ddashboard,name='ddashboard'),
    path('rdashboard/',views.rdashboard,name='rdashboard'),
    #-----------Success urls----------------------------
    path('success/<str:source>/',views.success,name='success'),
]