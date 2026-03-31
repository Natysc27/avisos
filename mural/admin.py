from django.contrib import admin
from .models import Categoria, Aviso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_criacao')
    list_filter = ('categoria', 'data_criacao')
    search_fields = ('titulo', 'conteudo')
    date_hierarchy = 'data_criacao'