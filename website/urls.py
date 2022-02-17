from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', LogoutView.as_view(next_page="home"), name='logoutPage'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('forum/', views.forum, name='forum'),
    path('games/<int:pk>', views.gameDetails, name='gameDetails'),
    path('addRate/<int:pk>', views.addRate, name='addRate'),
    path('addComment/<int:pk>', views.addComment, name='addComment'),
    path('searchGame', views.search, name='search'),
    path('ranking/', views.ranking, name='ranking')
]
