from django.shortcuts import render
from .models import Produto

# aqui estamos consultando o banco e retornando uma lista de produtos que será enviado para o templatee exbido na tela.
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', 
                  {'produtos': produtos}
                  )