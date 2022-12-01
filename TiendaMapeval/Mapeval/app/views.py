from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from app.models import Cliente, Producto, Formulario, Empleados
from django.contrib.auth import authenticate, login, logout


# templates sin recepcion de datos

def inicio(request):
    return render(request,'app/home.html')




#Productos
def ingresoProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        imagen = request.FILES.get('image')
        prod = Producto.objects.create(
            nombreproducto=nombre,
            precioproducto=precio, 
            cantidadproducto=cantidad,
            descripcionproducto=descripcion,
            estadoproducto=estado,
            imagenproducto=imagen,
            )
        prod.save()
        return redirect('/productosIngresados')
        
    elif request.method == 'GET':
        return render(request, 'app/productosIngresados.html')
        
def verProductosIngresados(request):
    prod = Producto.objects.all()
    data = {"producto":prod}
    return render(request, 'app/productosIngresados.html',data)
    
def productos(request):
    prod = Producto.objects.all()
    data= {"producto":prod}
    return render(request, "app/productos.html",data)

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, idproducto=id)
    producto.delete()  
    return redirect("/productosIngresados")

def Detalles(request,nombre):
    prod = Producto.objects.get(nombreproducto= nombre)
    data = {"producto":prod}
    return render(request, 'App/detalleProducto.html',data)

# Clientes y empleados
def registroCliente(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        primerNombre = request.POST.get("primerNombre")
        segundoNombre = request.POST.get("segundoNombre")
        apellidoPaterno = request.POST.get("apellidoPaterno")
        apellidoMaterno = request.POST.get("apellidoMaterno")
        direccion = request.POST.get("Direccion")
        telefono = request.POST.get("Telefono")
        correo = request.POST.get("email")
        contraseña = request.POST.get("contraseña")
        cliente = Cliente( rut, primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, direccion , telefono , correo, contraseña )
        cliente.save()
        user = User.objects.create_user(correo,correo, contraseña)
        user.first_name = primerNombre
        user.last_name = apellidoPaterno
        user.save()
    return render(request, 'app/registro.html')

def registroEmpleado(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        primerNombre = request.POST.get("primerNombre")
        segundoNombre = request.POST.get("segundoNombre")
        apellidoPaterno = request.POST.get("apellidoPaterno")
        apellidoMaterno = request.POST.get("apellidoMaterno")
        correo = request.POST.get("email")
        contraseña = request.POST.get("contraseña")
        direccion = request.POST.get("Direccion")
        telefono = request.POST.get("Telefono")
        empleado = Empleados( rut, primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, correo , contraseña, direccion, telefono)
        empleado.save()
        user = User.objects.create_user(correo,correo, contraseña)
        user.is_staff=1
        user.is_superuser=1
        user.first_name = primerNombre
        user.last_name = apellidoPaterno
        user.save()
    return render(request, 'app/registro.html')

def verUsuarios(request):
    empleado= Empleados.objects.all()
    cliente= Cliente.objects.all()
    data={"empleados":empleado,'cliente':cliente}
    return render(request,'app/verUsuarios.html',data)





def eliminar_cliente(request,rut):
    cliente= Cliente.objects.get(rut=rut)
    cliente.delete()
    return redirect('/verUsuarios')

def eliminar_empleado(request,rut):
    empleado= Empleados.objects.get(rut=rut)
    empleado.delete()
    return redirect('/verUsuarios')



# autenticacion inicio sesion
def iniciarSesion(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        contraseña = request.POST.get("contraseña")
        user = authenticate(request, username=correo, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect("/productos")
    return render(request, 'app/login.html')

def cerrarSesion(request):
    logout(request)
    return redirect("/")


def modificarProducto(request,id=None):
    if request.method == "POST":
        id = request.POST.get('id')
        prod = Producto.objects.get(id=id)
        prod.nombreproducto = request.POST.get("nombre")
        prod.precioproducto = request.POST.get('precio')
        prod.cantidadproducto = request.POST.get("cantidad")
        prod.estadoproducto = request.POST.get('estado')
        prod.save()
        return redirect('/productosIngresados')
    elif request.method == "GET":
        prod= Producto.objects.get(id=id)
        data = {"producto":prod}
        return render(request,"app/modificarProducto.html",data)

# contacto

def formulario(request): 
    if request.method == "POST":
        rutCliente = request.POST.get("rut")
        nombreCliente = request.POST.get("nombre")
        apellidoCliente = request.POST.get("apellido")
        correoCliente = request.POST.get("correo")
        mensajeCliente = request.POST.get("mensaje")
        formu = Formulario(rutCliente,nombreCliente,apellidoCliente,correoCliente,mensajeCliente)
        formu.save()
    return render(request, 'app/Formulario.html')




def verFormulario(request):
    formu= Formulario.objects.all()
    data={'formulario':formu}
    return render(request,"app/Formulario.html",data)





def carrito(request):
    return render(request,'app/carrito.html')