from rest_framework import viewsets #cria o pacote de visulização
from aluraflix_api.models import videos #importa o modelo do banco de dados
from aluraflix_api.serializer import VideoSerializer #importa nosso serializador

class VideosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os videos'''
    queryset = videos.objects.all() #filtro seria aqui
    serializer_class = VideoSerializer
