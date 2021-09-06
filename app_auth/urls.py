from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.login_blog, name="login-blog"),
    path('inscription/', views.register_blog, name="register"),
    path('deconnexion/', views.register_blog, name="logout"),
]
