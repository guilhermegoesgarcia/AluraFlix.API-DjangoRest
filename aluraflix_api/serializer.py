from rest_framework import serializers

from aluraflix_api.models import videos,categorias

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields =['id','titulo','descricao','url','categoriaId']

# https://stackoverflow.com/questions/60427872/django-updating-db-column-rest-framework


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = '__all__'

class ListaVideosDeCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields = '__all__'