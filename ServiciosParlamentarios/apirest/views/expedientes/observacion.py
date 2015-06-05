from rest_framework import viewsets, filters
from apirest.models.expedientes.observacion import Observacion 
from apirest.serializers.expedientes.observacion import ObservacionSerializer
from apirest.filters.expedientes.observacion_filter import ObservacionFilter

class ObservacionViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Observacion
    queryset = Observacion.objects.all()
    serializer_class = ObservacionSerializer
    filter_class = ObservacionFilter
    ordering_fields = '__all__'
    search_fields = ('observacion','fk_despacho')
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todas las observaciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una observacion solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)