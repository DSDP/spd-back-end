from rest_framework import serializers
from apirest.models.expedientes.expediente import Expediente

class ExpedienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expediente
        fields = ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces')