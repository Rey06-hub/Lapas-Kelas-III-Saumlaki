from django.shortcuts import render
from .models import HomepageStat
from news.models import News

def home(request):
    # Ambil statistik pertama (atau buat default jika belum ada)
    stat = HomepageStat.objects.first()
    if not stat:
        stat = HomepageStat.objects.create()  # buat data default 0

    # Data untuk warga binaan
    warga_data = {
        'narapidana': stat.narapidana,
        'tahanan': stat.tahanan,
        'titipan': stat.titipan,
        'total': stat.narapidana + stat.tahanan + stat.titipan,
    }

    # Data lainnya
    petugas_data = {'jumlah': stat.petugas_jaga}
    program_data = {'jumlah': stat.program_pembinaan_aktif}
    kepuasan_data = stat.survey_kepuasan

    # Link survey (misal dari model konfigurasi atau hardcode dulu)
    survey_link = "https://link-ikm-lapas.com"  # bisa diubah nanti

    # Ambil berita terbaru (gunakan field 'status' jika ada, atau filter lain)
    try:
        latest_news = News.objects.filter(status='published').order_by('-published_date')[:6]
    except:
        latest_news = []

    # Data dummy untuk dokumen (3 dokumen terbaru) - bisa diganti dengan model nanti
    latest_documents = [
        {
            'id': 1,
            'title': 'Prosedur Operasional Standar (POS) Lapas',
            'description': 'Pedoman pelaksanaan kegiatan harian di Lembaga Pemasyarakatan',
            'category': 'Prosedur',
            'upload_date': '10 Februari 2026',
            'file_size': '2.5 MB',
            'file_type': 'PDF',
            'icon_class': 'fa-file-pdf text-danger'
        },
        {
            'id': 2,
            'title': 'Laporan Tahunan 2025',
            'description': 'Laporan kinerja dan kegiatan Lapas Kelas III Saumlaki tahun 2025',
            'category': 'Laporan',
            'upload_date': '15 Januari 2026',
            'file_size': '5.1 MB',
            'file_type': 'PDF',
            'icon_class': 'fa-file-pdf text-danger'
        },
        {
            'id': 3,
            'title': 'Formulir Permohonan Kunjungan',
            'description': 'Formulir untuk permohonan kunjungan keluarga ke Lapas',
            'category': 'Formulir',
            'upload_date': '20 Januari 2026',
            'file_size': '0.5 MB',
            'file_type': 'DOCX',
            'icon_class': 'fa-file-word text-primary'
        },
    ]

    # Gabungkan semua context
    context = {
        'warga': warga_data,
        'petugas': petugas_data,
        'program': program_data,
        'kepuasan': kepuasan_data,
        'survey_link': survey_link,
        'latest_news': latest_news,
        'latest_documents': latest_documents,
    }

    return render(request, 'pages/home.html', context)

def about_us(request):
    return render(request, 'pages/about_us.html')

def contact(request):
    return render(request, 'pages/contact.html')