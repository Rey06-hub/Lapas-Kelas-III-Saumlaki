# news/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import News, Category
from datetime import datetime

def news_list(request):
    # Inisialisasi query
    news_list = News.objects.filter(status='published')
    
    # SEARCH: Filter berdasarkan kata kunci di judul
    search_query = request.GET.get('q')
    if search_query:
        news_list = news_list.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # FILTER KATEGORI: Filter berdasarkan kategori
    category_id = request.GET.get('category')
    category_name = None
    if category_id:
        try:
            category = Category.objects.get(id=category_id)
            news_list = news_list.filter(category=category)
            category_name = category.name
        except Category.DoesNotExist:
            pass
    
    # SORTING: Urutkan berdasarkan parameter
    sort_by = request.GET.get('sort', 'latest')
    if sort_by == 'popular':
        news_list = news_list.order_by('-views', '-published_date')
    else:  # latest
        news_list = news_list.order_by('-published_date')
    
    # PAGINATION
    paginator = Paginator(news_list, 6)  # 6 berita per halaman
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    # KATEGORI dengan jumlah berita
    categories = Category.objects.all()
    for category in categories:
        category.news_count = News.objects.filter(
            category=category, 
            status='published'
        ).count()
    
    # BERITA POPULER (3 teratas berdasarkan views)
    popular_news = News.objects.filter(
        status='published'
    ).order_by('-views')[:3]
    
    # BERITA UTAMA untuk carousel (3 terbaru)
    featured_news = News.objects.filter(
        status='published'
    ).order_by('-published_date')[:3]
    
    # STATISTIK
    total_news_count = News.objects.filter(status='published').count()
    current_year = datetime.now().year
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'popular_news': popular_news,
        'featured_news': featured_news,
        'total_news_count': total_news_count,
        'current_year': current_year,
        'category_id': int(category_id) if category_id else None,
        'category_name': category_name,
    }
    
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status='published')
    
    # Tambah view count
    news.views += 1
    news.save(update_fields=['views'])
    
    # Berita terkait (dari kategori yang sama)
    related_news = News.objects.filter(
        category=news.category,
        status='published'
    ).exclude(id=news.id).order_by('-published_date')[:3]
    
    # Previous and next news
    previous_news = News.objects.filter(
        published_date__lt=news.published_date,
        status='published'
    ).order_by('-published_date').first()
    
    next_news = News.objects.filter(
        published_date__gt=news.published_date,
        status='published'
    ).order_by('published_date').first()
    
    return render(request, 'news/news_detail.html', {
        'news': news,
        'related_news': related_news,
        'previous_news': previous_news,
        'next_news': next_news,
    })