# documents/models.py
from django.db import models

class DocumentCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class PublicDocument(models.Model):
    DOCUMENT_TYPES = [
        ('surat', 'Surat Resmi'),
        ('laporan', 'Laporan'),
        ('pengumuman', 'Pengumuman'),
        ('lainnya', 'Lainnya'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    document_file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-upload_date']