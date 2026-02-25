# documents/views.py - SOLUSI HYBRID
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from .models import PublicDocument, DocumentCategory

def document_list(request):
    # Ambil semua dokumen yang dipublikasikan
    documents = PublicDocument.objects.filter(is_published=True)
    
    # Filter berdasarkan kategori
    category_slug = request.GET.get('category')
    if category_slug and category_slug != '':
        documents = documents.filter(category__slug=category_slug)
    
    # Filter berdasarkan tipe dokumen
    doc_type = request.GET.get('type')
    if doc_type and doc_type != '':
        documents = documents.filter(document_type=doc_type)
    
    # Hitung total
    total_count = documents.count()
    
    # Get categories with document count
    categories = DocumentCategory.objects.annotate(
        doc_count=Count('publicdocument')
    )
    
    # Get document type counts
    type_counts = {}
    for type_code, type_name in PublicDocument.DOCUMENT_TYPES:
        count = PublicDocument.objects.filter(
            document_type=type_code, 
            is_published=True
        ).count()
        type_counts[type_code] = {
            'name': type_name,
            'count': count
        }
    
    # Pagination
    paginator = Paginator(documents, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'document_types': PublicDocument.DOCUMENT_TYPES,
        'total_count': total_count,
        'type_counts': type_counts,
        'selected_category': category_slug,
        'selected_type': doc_type,
    }
    
    return render(request, 'documents/document_list.html', context)