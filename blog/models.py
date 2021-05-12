from django.db import models


# Create your models here.
class Publication(models.Model):
    nome_da_empresa = models.CharField(max_length=200)
    descrição_do_serviço = models.TextField()
    CNPJ = models.TextField()
    número_da_nota = models.CharField(max_length=256)
    data_e_hora_da_emissão = models.CharField(max_length=200)
    valor_da_nota = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)