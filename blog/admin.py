from django.contrib import admin
from blog.models import NotaFiscal


class PublicationAdmin(admin.ModelAdmin):
    date_hierarchy = 'data_publicacao'
    list_display = ('empresa', 'descricao', 'valor_nota','data_publicacao')
    list_filter = ('empresa' , 'cnpj')
    search_fields = ('empresa' , 'cnpj')


admin.site.register(NotaFiscal, PublicationAdmin)
# Register your models here.
