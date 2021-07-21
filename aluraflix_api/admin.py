from django.contrib import admin
from aluraflix_api.models import videos
# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','url')
    list_display_links = ('id','titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(videos,Videos)