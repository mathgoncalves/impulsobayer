from django.shortcuts import render
from blog.models import Publication


# Create your views here.
def show_index (request):
    title = "Today is a new day"
    return render (request,"index.html", {"name":title})


def show_publication_done (request):
    dados = {

        'nome_da_empresa': request.POST.get ('nome_da_empresa'),
        'descrição_do_serviço': request.POST.get('descrição_do_serviço'),
        'CNPJ': request.POST.get('CNPJ'),
        'número_da_nota': request.POST.get('número_da_nota'),
        'data_e_hora_da_emissão': request.POST.get('data_e_hora_da_emissão'),
        'valor_da_nota': request.POST.get('valor_da_nota ')

    }

    print(dados)

    publicacao = Publication(**dados)
    publicacao.save()

    return render(request,'publication_done.html',{'número_da_nota': publicacao.número_da_nota})