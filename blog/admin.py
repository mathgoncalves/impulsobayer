from django.contrib import admin
from blog.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('nome_da_empresa', 'descrição_do_serviço', 'valor_da_nota','publication_date')
    list_filter = ('nome_da_empresa', 'CNPJ')
    search_fields = ('nome_da_empresa', 'CNPJ')


admin.site.register(Publication, PublicationAdmin)
# Register your models here.
