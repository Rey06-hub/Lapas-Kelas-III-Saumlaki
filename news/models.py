# models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('news_list') + f'?category={self.id}'

class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    excerpt = models.TextField(blank=True, max_length=300)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news_items')
    author = models.CharField(max_length=100, default='Admin Lapas')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Buat excerpt otomatis jika kosong
        if not self.excerpt and self.content:
            self.excerpt = self.content[:300] + '...' if len(self.content) > 300 else self.content
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])
    
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])# models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('news_list') + f'?category={self.id}'

class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    excerpt = models.TextField(blank=True, max_length=300)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news_items')
    author = models.CharField(max_length=100, default='Admin Lapas')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Buat excerpt otomatis jika kosong
        if not self.excerpt and self.content:
            self.excerpt = self.content[:300] + '...' if len(self.content) > 300 else self.content
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])
    
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])