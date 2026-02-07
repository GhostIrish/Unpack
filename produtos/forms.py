from django import forms
from .models import Produto

# Formulário para o modelo Produto
class ProdutoForm(forms.ModelForm):
    class Meta: # Informa ao Django que este formulário é baseado no modelo Produto, para isso é utilizado a classe Meta.
        model = Produto
        fields = "__all__"  # Inclui todos os campos do modelo Produto