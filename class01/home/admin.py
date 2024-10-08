from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models

class TopicoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{
            'widget': TinyMCE()
        }
    }

class FerramentaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{
            'widget': TinyMCE()
        }
    }

# Register your models here.
admin.site.register(Categoria)
admin.site.register(AreaAtuacao)
admin.site.register(Topico)
admin.site.register(Ferramenta)
admin.site.register(Erro)
admin.site.register(Suporte)
