from django.db import models


class Inmueble(models.Model):
    inm_id = models.AutoField(primary_key=True)
    inm_nombre = models.CharField(max_length=50)
    inm_descripcion = models.TextField()
    inm_m2_construidos = models.FloatField()
    inm_m2_total = models.FloatField()
    inm_nro_estacionamientos = models.IntegerField()
    inm_nro_habitaciones = models.IntegerField(blank=True, null=True)
    inm_nro_banos = models.IntegerField()
    inm_direccion = models.CharField(max_length=50)
    inm_precio = models.IntegerField()
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, blank=True, null=True)
    tipoi_codigo = models.ForeignKey('TipoInmueble', on_delete=models.CASCADE, db_column='tipoi_codigo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmueble'


class Comuna(models.Model):
    comuna_id = models.CharField(primary_key=True, max_length=20)
    comuna_nombre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'comuna'


class TipoInmueble(models.Model):
    tipoi_codigo = models.AutoField(primary_key=True)
    tipoi_descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_inmueble'


class EstadoPropiedad(models.Model):
    estprop_id = models.AutoField(primary_key=True)
    estprop_descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_propiedad'


class TipoUsuario(models.Model):
    tipou_codigo = models.AutoField(primary_key=True)
    tipou_descripcion = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    usu_rut = models.CharField(primary_key=True, max_length=9)
    usu_nombre = models.CharField(max_length=50)
    usu_apellido_pat = models.CharField(max_length=50)
    usu_apellido_mat = models.CharField(max_length=50)
    usu_direccion = models.CharField(max_length=50)
    usu_telefono = models.CharField(20)
    usu_mail = models.CharField(max_length=30)
    tipou_codigo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='tipou_codigo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class InmuebleArrendatario(models.Model):
    inm = models.ForeignKey(Inmueble, on_delete=models.CASCADE, blank=True, null=True)
    usu_rut = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usu_rut', blank=True, null=True)
    ia_fecha_inicio = models.DateField(blank=True, null=True)
    ia_fecha_fin = models.DateField(blank=True, null=True)
    estprop = models.ForeignKey(EstadoPropiedad, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmueble_arrendatario'
        unique_together = (('inm', 'usu_rut'),)
