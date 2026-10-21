from django.contrib import admin

from .models import *


class EtapaTrilhaInline(admin.TabularInline):
    model = EtapaTrilha
    extra = 1
    autocomplete_fields = ['topico']


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'nivel_alvo', 'ordem', 'ativa')
    list_filter = ('ativa', 'nivel_alvo')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [EtapaTrilhaInline]


@admin.register(EtapaTrilha)
class EtapaTrilhaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'trilha', 'ordem', 'topico')
    list_filter = ('trilha',)
    search_fields = ('titulo',)


@admin.register(ProgressoUsuario)
class ProgressoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'etapa', 'concluida', 'updated_at')
    list_filter = ('concluida', 'etapa__trilha')


@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('nome_topico', 'nivel_experiencia', 'created_at')
    list_filter = ('nivel_experiencia', 'categorias')
    search_fields = ('nome_topico',)


admin.site.register(Categoria)
admin.site.register(AreaAtuacao)
admin.site.register(Ferramenta)
admin.site.register(Erro)
admin.site.register(Suporte)
