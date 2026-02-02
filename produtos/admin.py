from django.contrib import admin
from .models import Produto

# Registrando o modelo Produto para que ele possa ser gerenciado através do admin do Django.
admin.site.register(Produto)