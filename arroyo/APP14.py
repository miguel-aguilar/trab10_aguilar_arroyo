import  libreria
def opcion1():
#pedir el producto
#pedir la cantidad
#guardar datos en "listado.txt"
    producto=libreria.pedir_nombre("Ingrese el producto")
    cantidad=libreria.pedir_entero_positivo("ingrese la cantidad por comprar del  producto")
    contenido=producto+"-"+str(cantidad)+"\n"
    libreria.agregar_datos("listado.txt",contenido,"w")
    print("Su compra se guardo con exito")
#esta opcion te permmite mostrar los datos ingresados en el archivo "listado.txt"
def opcion2():
    datos=libreria.obtener_datos("listado.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")

#esta funcion mejorada te permite organizar los datos y separalos uno a uno
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("listado.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            producto, cantidad = item.split("-")
            msg="EL producto: {} "+"\n" + "Cantidad por comprar {}"
            producto=producto.replace("\n","")
            cantidad=cantidad.replace("\n","")
            print(msg.format(producto,cantidad))
        #fin_for
    else:
        print("No hay datos")

#El menu secundario
def opcionsub():
    opc=0
    max=3
    while(opc!=max):
        print("#########  CONDICION ECONOMICA  ###########")
        print("1. INTRODUCIR DATOS DEL COMPRADOR")
        print("2. MOSTRAR DATOS OBTENIDOS")
        print("3. DATOS ORDENADOS ")
        print("4. SALIR")
        print("#####################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,5)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()


def subopcion1():
#pedir el nombre
#pedir el apellido
#guardar datos en "datos_comprador.txt"
    nombre=libreria.pedir_nombre("Ingrese su nombre ")
    apellido=libreria.pedir_nombre("Ingrese su apellido ")
    contenido=nombre+"-"+apellido+"\n"
    libreria.agregar_datos("datos_comprador.txt",contenido,"w")
    print("Su compra se guardo con exito")

#esta opcion te permmite mostrar los datos ingresados en el archivo "listado.txt"
def subopcion2():
    datos=libreria.obtener_datos("datos_comprador.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")

def subopcion3():
    # 1. Abrir el archivo "datos_comprador.txt" y mostrar sus datos
    data=libreria.obtener_datos_lista("datos_comprador.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, apellido = item.split("-")
            msg="NOMBRE: {} "+"\n" + "APELLIDO {}"
            nombre=nombre.replace("\n","")
            apellido=apellido.replace("\n","")
            print(msg.format(nombre,apellido))
        #fin_for
    else:
        print("No hay datos")

# Menu principal
opc=0
max=5
while(opc!=max):
    print("================================================")
    print("================================================")
    print("********HACER LISTADO DE COMPRAS ***************")
    print("** 1. Productos por comprar                   **")
    print("** 2. cantidad de productos                   **")
    print("** 3. mostrar lista de compras                **")
    print("** 4. Introducir datos  del comprador         **")
    print("** 5. salir                                   **")
    print("================================================")
    print("================================================")
    opc=libreria.pedir_entero("ingrese opcion:",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        obtener_sum()
    if(opc==4):
        opcionsub()
