from django.contrib import admin

from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation', 'update', 'active')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'name', 'email', 'avaliacao', 'creation', 'update', 'active')
