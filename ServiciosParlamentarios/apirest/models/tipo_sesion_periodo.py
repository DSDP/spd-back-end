from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.periodo import Periodo

class TipoSesionPeriodo(models.Model):
    id = models.AutoField(primary_key=True,db_column='tipo_sesion_periodo_id')
    fk_periodo = models.ForeignKey(Periodo, db_column='fk_periodo')
    fecha_inicio = models.DateField(blank=True, null=True, db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True, db_column='ffin')
    tipo = models.TextField()
    
    class Meta:
        managed = False
        db_table = Constants().TIPO_SESION_PERIODO
        app_label = Constants().APIREST