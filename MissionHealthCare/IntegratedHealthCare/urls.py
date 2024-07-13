from django.urls import path
from .import views

urlpatterns=[
    #-----------signup urls----------------------------
    path('',views.psignup,name='psignup'),
    path('dsignup',views.dsignup,name='dsignup'),
    #-----------login urls----------------------------
    path('plogin/',views.plogin,name='plogin'),
    path('dlogin/',views.dlogin,name='dlogin'),
    #-----------Success urls----------------------------
    path('success/<str:source>/',views.success,name='success'),
]