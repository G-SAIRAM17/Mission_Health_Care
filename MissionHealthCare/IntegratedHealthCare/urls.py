from django.urls import path
from .import views

urlpatterns=[
    #-----------signup urls----------------------------
    path('',views.psignup,name='psignup'),
    path('dsignup',views.dsignup,name='dsignup'),
    path('rsignup',views.rsignup,name='rsignup'),
    path('lsignup',views.lsignup,name='lsignup'),
    path('asignup',views.asignup,name='asignup'),
    #-----------login urls----------------------------
    path('plogin/',views.plogin,name='plogin'),
    path('dlogin/',views.dlogin,name='dlogin'),
    path('rlogin/',views.rlogin,name='rlogin'),
    path('llogin/',views.llogin,name='llogin'),
    path('alogin/',views.alogin,name='alogin'),
    #-----------dashboard urls----------------------------
    path('pdashboard/<str:name>/',views.pdashboard,name='pdashboard'),
    path('dbashboard/<str:name>/',views.ddashboard,name='ddashboard'),
    path('rdashboard/<str:name>/',views.rdashboard,name='rdashboard'),
    path('ldashboard/<str:name>/',views.ldashboard,name='ldashboard'),
    path('adashboard/',views.adashboard,name='adashboard'),
    #-----------Success urls----------------------------
    path('psuccess/',views.psuccess,name='psuccess'),
    path('dsuccess/',views.dsuccess,name='dsuccess'),
    path('rsuccess/',views.rsuccess,name='rsuccess'),
    path('lsuccess/',views.lsuccess,name='lsuccess'),
    path('asuccess/',views.asuccess,name='asuccess'),
    #---------------Inside Patient Dashboard urls-------------------------
    path('pdoctor/<str:name>/',views.pdoctor,name='pdoctor'),
    path('phospital/<str:name>/',views.phospital,name='phospital'),
    path('doctors/<int:doctor_id>/book/<str:name>/', views.book_appointment, name='book_appointment'),
    path('doctors_list/<str:name>/<str:hname>/', views.doctors_list, name='doctors_list'),
    path('pupdate/<str:name>/',views.pupdate,name='pupdate'),
    #---------------Inside Doctor Dashboard urls-------------------------path('dtimeslots/<str:doctor_name>/', views.dtimeslots, name='dtimeslots')
    path('dtimeslots/<str:name>/', views.dtimeslots, name='dtimeslots')


]