from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home, about_us, contact  # Tambahkan contact

# Import views langsung untuk berita (tidak menggunakan include)
from news.views import news_list, news_detail
from documents.views import document_list  # Import views documents

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Halaman utama
    path('', home, name='home'),
    
    # Tentang Kami
    path('tentang-kami/', about_us, name='about_us'),
    
    # Kontak
    path('kontak/', contact, name='contact'),
    
    # Berita
    path('berita/', news_list, name='news_list'),
    path('berita/<slug:slug>/', news_detail, name='news_detail'),
    
    # Dokumen - menggunakan path langsung
    path('dokumen/', document_list, name='document_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)