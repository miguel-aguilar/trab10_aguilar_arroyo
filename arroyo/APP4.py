import libreria
def opcion1():
#pedir el roducto
#pedir la cantidad del producto
#guardar datos en cmpras.txt
    producto=libreria.pedir_nombre("Ingrese el producto")
    cantidad=libreria.pedir_entero_positivo("ingrese la cantidad por comprar del  producto")
    contenido=producto+"-"+str(cantidad)+"\n"
    libreria.agregar_datos("listado.txt",contenido,"a")
    print("Su compra se guardo con exito")
#pComprobando si la funcion existe
def opcion2():
    datos=libreria.obtener_datos("compras.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
def obtener_sum():
    # 1. Abrir el archivo listado.txt y mostrar sus datos
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
#menu principal,donde se puede elegir opciones
opc=0
max=4
while(opc!=max):
    print("************************************************")
    print("********HACER LISTADO DE COMPRAS **************")
    print("** 1. Productos por comprar                  **")
    print("** 2. cantidad de productos                  **")
    print("** 3. mostrar lista de compras               **")
    print("** 4. salir                                  **")
    print("************************************************")
    print("************************************************")
    opc=libreria.pedir_entero("ingrese opcion:",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        obtener_sum()



