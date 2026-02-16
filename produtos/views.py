from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm  
from core.views import home 
from django.contrib.auth.decorators import login_required

# aqui estamos consultando o banco e retornando uma lista de produtos que será enviado para o templatee exbido na tela.
@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', 
                  {'produtos': produtos}
                  )

@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redireciona para a página de lista de produtos após criar o produto
    form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redireciona para a página de lista de produtos após editar o produto
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id) # Obtém o produto pelo id ou retorna 404 se não encontrado
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')  # Redireciona para a página de lista de produtos após excluir o produto
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})