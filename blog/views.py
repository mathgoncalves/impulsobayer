from django.shortcuts import render
from blog.models import NotaFiscal


# Create your views here.
def show_index (request):
    title = "Today is a new day"
    return render (request,"index.html", {"name":title})


def show_publication_done (request):
    dados = {

        'empresa': request.POST.get ('empresa'),
        'descricao': request.POST.get('descricao'),
        'cnpj': request.POST.get('cnpj'),
        'nota': request.POST.get('nota'),
        'data_emissao': request.POST.get('data_emissao'),
        'valor_nota': request.POST.get('valor_nota')

    }

    print(dados)

    publicacao = NotaFiscal(**dados)
    publicacao.save()

    return render(request,'publication_done.html',{'nota': publicacao.nota})