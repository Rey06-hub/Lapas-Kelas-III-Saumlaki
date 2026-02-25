from django.contrib import admin
from .models import HomepageStat

@admin.register(HomepageStat)
class HomepageStatAdmin(admin.ModelAdmin):
    list_display = ('narapidana', 'tahanan', 'titipan', 'petugas_jaga', 
                    'program_pembinaan_aktif', 'survey_kepuasan')
    # Jika ingin hanya satu data, bisa gunakan fieldsets atau disable add another