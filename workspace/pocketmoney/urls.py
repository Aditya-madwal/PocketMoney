from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<int:pk>', views.deleteview, name = 'delete'),
    path('delete_t/<int:pk>', views.delete_tview, name = 'delete_t'),
    path('reset/<int:pk>', views.resetview, name = 'reset'),
    path('', views.homeview, name = 'home'),
    path('wallet/<int:pk>/', views.walletview, name = 'wallet'),
    path('login/', views.loginview, name = 'login'),
    path('signup/', views.signupview, name = 'signup'),
    path('logout/', views.logoutview, name = 'logout'),
]
