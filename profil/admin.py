from django.contrib import admin

# Register your models here.

from .models import Barang, Jenis

class BarangAdmin(admin.ModelAdmin):
    list_display = ['kdbrg', 'nama','stok','harga','jenis_id']
    search_fields = ('kdbrg','nama','jenis_id__nama')
    list_filter = ['jenis_id',]
    list_per_page = 3


admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)