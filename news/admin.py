# admin.py
from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'news_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
    def news_count(self, obj):
        return obj.news_items.count()
    news_count.short_description = 'Jumlah Berita'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_date', 'status', 'views', 'is_featured')
    list_filter = ('status', 'category', 'published_date', 'is_featured')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views', 'published_date', 'updated_date')
    fieldsets = (
        ('Informasi Berita', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'image')
        }),
        ('Kategori dan Status', {
            'fields': ('category', 'author', 'status', 'is_featured')
        }),
        ('Statistik', {
            'fields': ('views', 'published_date', 'updated_date')
        }),
    )
    
    actions = ['make_published', 'make_draft', 'mark_featured']
    
    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Publikasi berita terpilih"
    
    def make_draft(self, request, queryset):
        queryset.update(status='draft')
    make_draft.short_description = "Jadikan draft"
    
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)
    mark_featured.short_description = "Tandai sebagai berita utama"