from django.db import models


class Carrocompra(models.Model):
    producto_id = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=45, blank=True, null=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    estado_producto = models.CharField(max_length=45, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    cliente_rut = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='Cliente_rut')  # Field name made lowercase.
    ventas_idventas = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='Ventas_idVentas')  # Field name made lowercase.
    producto_idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carrocompra'
        unique_together = (('producto_id', 'cliente_rut', 'ventas_idventas', 'producto_idproducto'),)


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    primernombre = models.CharField(db_column='primerNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=45)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Empleados(models.Model):
    rut = models.CharField(primary_key=True, max_length=45)
    primernombre = models.CharField(db_column='primerNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=45)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=45)  # Field name made lowercase.
    correo = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'
        unique_together = (('rut', 'apellidomaterno'),)


class Formulario(models.Model):
    rutcliente = models.CharField(primary_key=True, max_length=45)
    nombrecliente = models.CharField(max_length=45, blank=True, null=True)
    apellidocliente = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    mensajecliente = models.CharField(max_length=435, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'formulario'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precioproducto = models.CharField(db_column='precioProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cantidadproducto = models.CharField(db_column='cantidadProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcionproducto = models.CharField(db_column='descripcionProducto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    estadoproducto = models.CharField(db_column='estadoProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagenproducto = models.ImageField(upload_to='productos', null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Ventas(models.Model):
    idventas = models.PositiveIntegerField(db_column='idVentas', primary_key=True)  # Field name made lowercase.
    n_producto = models.CharField(max_length=45, blank=True, null=True)
    c_producto = models.CharField(max_length=45, blank=True, null=True)
    p_producto = models.CharField(max_length=45, blank=True, null=True)
    d_producto = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'