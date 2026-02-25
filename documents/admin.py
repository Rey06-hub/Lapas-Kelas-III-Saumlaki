# documents/admin.py (SIMPLE VERSION)
from django.contrib import admin
from .models import DocumentCategory, PublicDocument

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PublicDocument)
class PublicDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'category', 'upload_date', 'is_published']
    list_filter = ['document_type', 'category', 'is_published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']