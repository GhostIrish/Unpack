from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do produto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição do produto'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00'
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantidade em estoque'
            }),
        }