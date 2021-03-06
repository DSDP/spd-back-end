from rest_framework import serializers
from apirest.models.organismos.bloques.bloque_estructura import BloqueEstructura
from apirest.serializers.individuos.legislador import LegisladorSerializer

class BloqueEstructuraSerializer(serializers.ModelSerializer):
    
    fk_legislador = LegisladorSerializer()
    
    class Meta:
        model = BloqueEstructura
        fields = ('id','fk_legislador','cargo','cargo_muestra_como','jerarquia','estado','fecha_desde','fecha_hasta')
    