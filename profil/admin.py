from django.contrib import admin

# Register your models here.

from .models import Barang, Jenis, About

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg','nama','stok','harga','link_gbr','tgl_input','id_jenis')
    search_fields = ('kdbrg','nama', 'id_jenis__nama')
    list_per_page = 3
    list_filter = ('id_jenis__nama',)


admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)
