from django.urls import path
from login import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('home_view/', views.home_view, name="home"),
    path('logout_view/',views.logout_view, name="logout_view"),
]