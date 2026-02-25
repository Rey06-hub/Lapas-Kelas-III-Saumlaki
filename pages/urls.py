# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tentang-kami/', views.about_us, name='about_us'),
    path('berita/', views.news_list, name='news_list'),
    # TAMBAHKAN INI:
    path('dokumen/', views.document_list, name='document_list'),  # ← BARU
    path('kontak/', views.contact, name='contact'),
    # Tambahkan ini juga untuk slug berita jika ada:
    path('berita/<slug:slug>/', views.news_detail, name='news_detail'),
]