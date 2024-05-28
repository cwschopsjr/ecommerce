from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInLine
    ]

class ProdutoVariacao(admin.ModelAdmin):
    list_display = ['produto', 'nome', 'get_preco_formatado', 'get_preco_promocional_formatado']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao, ProdutoVariacao)
