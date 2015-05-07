from rest_framework.compat import django_filters
from apirest.models.expedientes.expediente import Expediente

class ExpedienteFilter(django_filters.FilterSet):
    
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    codigoOrigen = django_filters.CharFilter(lookup_type='icontains',name="codigoorigen")
    tipoCamara = django_filters.CharFilter(lookup_type='icontains',name="tipocamara")
    codigoExp = django_filters.CharFilter(lookup_type='icontains',name="codigoexp")
    codigoNum = django_filters.CharFilter(lookup_type='icontains',name="codigonum")
    codigoAnio = django_filters.CharFilter(lookup_type='icontains',name="codigoanio")
    fechaCaducidad = django_filters.DateFilter(name="fechacaducidad")
    fechaDesde = django_filters.DateFilter(name="fecha", lookup_type='gte')
    fechaHasta = django_filters.DateFilter(name="fecha", lookup_type='lte')
    periodo = django_filters.NumberFilter(name="periodo")
    
    # Firmante filters
    firm_persona_fisica_id = django_filters.CharFilter(name="firmantes__persona_fisica_id")
    firm_orden = django_filters.CharFilter(name="firmantes__orden")
    firm_cargo = django_filters.CharFilter(name="firmantes__cargo")
    firm_cargo_tipo = django_filters.CharFilter(name="firmantes__cargo_tipo")
    firm_nombre_leg_func = django_filters.CharFilter(name="firmantes__nombre_leg_func")
    
    # Giro filters
    giro_comision_id = django_filters.CharFilter(name="giros__comision_id")
    giro_comision_nombre = django_filters.CharFilter(name="giros__comision_nombre")
    giro_comision_nombre_corto = django_filters.CharFilter(name="giros__comision_nombre_corto")
    
 
    class Meta:
        model = Expediente
        fields = ['tipo','codigoOrigen','tipoCamara','codigoExp','codigoNum','codigoAnio','fechaDesde',
                  'fechaHasta','fechaCaducidad','periodo','firm_orden','firm_cargo','firm_cargo_tipo',
                  'firm_persona_fisica_id','firm_nombre_leg_func','giro_comision_id','giro_comision_nombre',
                  'giro_comision_nombre_corto']
        order_by = True
        

# CODIGO PRUEBAS INICIALES
        
# Expediente filters
#     EXPEDIENTE_CHOICES = (  ('PROYECTO', 'proyecto'),
#                             ('COMUNICACION', 'comunicacion'),
#                             ('OBSERVACION', 'observacion'),
#                             ('COMUNICACION_PEN', 'comunicacion_pen',),
#                             ('SOLICITUD', 'solicitud',),)

#     tipo = django_filters.MultipleChoiceFilter(choices=EXPEDIENTE_CHOICES,name="tipo")
#     def filter_by_date_range(self, qs, what):
#         if what:
#             return qs.filter(**{'total_budget__range': (int(what.start) if what.start else 0, int(what.stop) if what.stop else sys.maxint)})
#         return qs


#         fields = ['tipo','tipo_proy','codigo_origen','tipo_camara','periodo', 'fecha_desde', 'fecha_hasta',# expedinte  
#                   'firm_orden','firm_cargo_pf_id','firm_apellido', #fimante filters
#                   ]   

#     firm_caracter = django_filters.CharFilter(name="firmantes__caracter")
#     firm_nota = django_filters.CharFilter(name="firmantes__nota")
#     firm_cargo_pf_id = django_filters.CharFilter(name="firmantes__cargo_persona_fisica_firma_expediente_id")
#     firm_apellido = django_filters.CharFilter(lookup_type='icontains',name="firmantes__fk_cargo_persona_fisica__fk_persona_fisica__historial__apellido")