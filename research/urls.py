from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('register/', views.RegisterView, name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('about/', views.aboutView, name="about"),
]