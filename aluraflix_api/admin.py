from django.contrib import admin
from aluraflix_api.models import videos,categorias
# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','url',)
    list_display_links = ('id','titulo',)

    list_per_page = 20

admin.site.register(videos,Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo','cor',)
    list_display_links = ('id', 'titulo',)

    list_per_page = 20

admin.site.register(categorias, Categorias)