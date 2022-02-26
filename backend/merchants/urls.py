from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginMerchant, name='login'),
    path('logout/', views.logOutMerchant, name='logout'),
    path('register/', views.registerMerchant, name='register')
]
