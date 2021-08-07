from rest_framework import viewsets, status, generics, filters #cria o pacote de visulização
from rest_framework.response import Response
from aluraflix_api.models import videos,categorias #importa o modelo do banco de dados
from aluraflix_api.serializer import VideoSerializer,CategoriasSerializer, ListaVideosDeCategoriaSerializer #importa nosso serializador


class VideosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os videos'''
    queryset = videos.objects.all() #filtro seria aqui
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo','descricao']

#https://cheat.readthedocs.io/en/latest/django/drf_serializers.html
    # o link acima mostra como resolver alguns problemas enfrentados no desenvolvimento da função a baixo..
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        try:
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data= {'detail':'Video not found'})

    def destroy(self, request, *args, **kwargs):
        ''' Deletand o video'''
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data= {'detail':'Video not found'})

        return Response(status=status.HTTP_200_OK, data={'detail':'Video successfuly deleted'})




class CategoriasViewsSet(viewsets.ModelViewSet):

    queryset = categorias.objects.all()
    serializer_class = CategoriasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        try:
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Category not found'})

    def destroy(self, request, *args, **kwargs):
        """Deleting a video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Category not found"})

        return Response(status=status.HTTP_200_OK, data={"detail": "Category successfuly deleted"})

class ListaVideosDeCategoria(generics.ListAPIView):
    '''Lista das categorias dos videos'''

    def get_queryset(self):
        queryset = videos.objects.filter(categoriaId=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosDeCategoriaSerializer