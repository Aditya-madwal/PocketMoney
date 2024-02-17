from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('delete/<str:pk>', views.deleteview, name = 'delete'),
    path('', views.homeview, name = 'home'),
    # path('wallet/<str:pk>/', views.walletview, name = 'wallet'),
    path('login/', views.loginview, name = 'login'),
    path('signup/', views.signupview, name = 'signup'),
]
