from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('add_book/', views.add_book, name='add_book'),
    path('assign_book/<int:user_id>/', views.assign_book, name='assign_book'),
    path('', views.home, name='home'),
    path('search_books/', views.search_books, name='search_books'),
    path('user_list/', views.user_list, name='user_list'),
]
