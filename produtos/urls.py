from django.urls import path
from .views import lista_produtos, criar_produto, editar_produto


# importa a view lista_produtos e a associa a url raiz deste app (produtos/)
urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('cadastrar/', criar_produto, name='criar_produto'),
    path("editar/<int:id>/", editar_produto, name="editar_produto"),
]