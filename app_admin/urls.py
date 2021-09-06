from django.urls import path
from . import views

urlpatterns = [
    path('app_admin/', views.dashbord, name="dashbord"),
    path('mes_articles/', views.user_articles, name="mes_articles"),
    path('ajouter-article/', views.AddArticle.as_view(), name="add-article"),
    path('update-article/<int:pk>', views.UpdateArticle.as_view(), name="update-article"),
    path('delete-article/<int:pk>', views.DeleteArticle.as_view(), name="delete-article"),
]
