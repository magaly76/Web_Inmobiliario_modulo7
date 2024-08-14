from .models import Inmueble, Comuna, Usuario, TipoInmueble, TipoUsuario, EstadoPropiedad, InmuebleArrendatario
from datetime import date

def crear_comuna(comuna_id, comuna_nombre):
    comuna = Comuna(
        comuna_id=comuna_id,
        comuna_nombre=comuna_nombre
    )
    comuna.save()

def crear_tipo_inmueble(tipoi_descripcion):
    tipo_inmueble=TipoInmueble(tipoi_descripcion=tipoi_descripcion)
    tipo_inmueble.save()

def crear_tipo_usuario(tipou_descripcion):
    tipo_usuario=TipoUsuario(tipou_descripcion=tipou_descripcion)
    tipo_usuario.save()

def crear_estado_propiedad(estprop_descripcion):
    estado_propiedad=EstadoPropiedad(estprop_descripcion=estprop_descripcion)
    estado_propiedad.save()

def crear_usuario(usu_rut, usu_nombre, usu_apellido_pat, usu_apellido_mat, usu_direccion, usu_telefono, usu_mail, tipou_codigo):
    usuario= Usuario(
        usu_rut=usu_rut,
        usu_nombre= usu_nombre,
        usu_apellido_pat=usu_apellido_pat,
        usu_apellido_mat=usu_apellido_mat,
        usu_direccion=usu_direccion,
        usu_telefono=usu_telefono,
        usu_mail=usu_mail,
        tipou_codigo=tipou_codigo
    )
    usuario.save()

def crear_inmueble(inm_nombre, inm_descripcion, inm_m2_construidos, inm_m2_totales, inm_nro_estacionamientos, inm_nro_habitaciones, inm_nro_banos, inm_direccion, inm_precio, comuna_id, tipoi_codigo):
    inmueble=Inmueble(
        inm_nombre=inm_nombre,
        inm_descripcion=inm_descripcion,
        inm_m2_construidos=inm_m2_construidos,
        inm_m2_totales=inm_m2_totales,
        inm_nro_estacionamientos=inm_nro_estacionamientos,
        inm_nro_habitaciones=inm_nro_habitaciones,
        inm_nro_banos=inm_nro_banos,
        inm_direccion=inm_direccion,
        inm_precio=inm_precio,
        comuna_id=comuna_id,
        tipoi_codigo=tipoi_codigo
    )
    inmueble.save()

def crear_inmuemble_arrendatario(inm_id, usu_rut, estprop_id):
    inmueble_arrendatario=InmuebleArrendatario(
        inm_id=inm_id,
        usu_rut=usu_rut,
        ia_fecha_inicio=date.today(),
        ia_fecha_fin=date.today(),
        estprop_id=estprop_id
    )
    inmueble_arrendatario.save()


    