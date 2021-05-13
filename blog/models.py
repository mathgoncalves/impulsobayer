from django.db import models


# Create your models here.
class NotaFiscal(models.Model):
    empresa = models.CharField(max_length=200)
    descricao = models.TextField()
    cnpj = models.TextField()
    nota = models.CharField(max_length=256)
    data_emissao = models.CharField(max_length=200)
    valor_nota = models.FloatField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)