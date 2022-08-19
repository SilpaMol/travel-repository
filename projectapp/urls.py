from . import views
from django.urls import path

urlpatterns = [

    path('',views.demoproject,name='demoproject'),
    # path('add/',views.addition,name='addition'),
    # path('abcd/',views.abcd,name='abcd.html')
    ]