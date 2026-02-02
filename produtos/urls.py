from django.urls import path
from .views import lista_produtos


# importa a view lista_produtos e a associa a url raiz deste app (produtos/)
urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
]