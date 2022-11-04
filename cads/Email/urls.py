from django.urls import path
from . import views

urlpatterns =[    
    path('',views.email,name = 'email'),
    path('index/', views.index, name='index'),
    path('index/send/', views.send,name = 'send'),
    path('register_users/', views.register_users, name = 'register_users'),
    path('register_users/add_registration/', views.add_registration, name = 'add_registration')

]