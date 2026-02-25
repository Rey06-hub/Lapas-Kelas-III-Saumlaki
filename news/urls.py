# urls.py
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('berita/', views.news_list, name='news_list'),
    path('berita/<slug:slug>/', views.news_detail, name='news_detail'),
]