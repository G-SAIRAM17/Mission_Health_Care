from django.urls import path
from .import views

urlpatterns=[
    path('',views.psignup,name='psignup'),
    path('plogin/',views.plogin,name='plogin'),
    path('psuccess/',views.psuccess,name='psuccess'),
]