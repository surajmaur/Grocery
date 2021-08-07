from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reg/', views.reg, name="reg"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('add/', views.addpage, name="add"),
    path('updategroce/<Groce_id>/', views.updateGroce, name="updategroce"),
    path('grocedelete/<Groce_id>/', views.DeleteGroce, name="deletegroce"),
]   