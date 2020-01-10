import libreria
def opcion1():
#pedir el roducto
#pedir el costo
#guardar datos en cmpras.txt
    producto=libreria.pedir_nombre("Ingrese el producto")
    costo=libreria.pedir_entero_positivo("ingrese el costo del producto")
    contenido=producto+"-"+str(costo)+"\n"
    libreria.agregar_datos("compras.txt",contenido,"a")
    print("Su compra se guardo con exito")

#Mediante esta funcion se optendras los datos ingresdos
def opcion2():
    datos=libreria.obtener_datos("compras.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")

#Mediante esta funcion se optendras los datos ingresdos y ordenados
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("compras.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            producto, costo = item.split("-")
            msg="EL producto {} tiene como precio unitario {}"
            producto=producto.replace("\n","")
            costo=producto.replace("\n","")
            print(msg.format(producto, costo))
        #fin_for
    else:
        print("No hay datos")
def subopcion1():
    print("Usted ha escogido el lugar de comprar : METRO")
def subopcion2():
    print("Usted ha escogido el lugar de comprar : TOTTUS")
def subopcion3():
    print("Usted ha escogido el lugar de comprar : PRECIO UNO")
def subopcion4():
    print("Usted ha escogido el lugar de comprar : SUPER")

#Elegir una opcion, donde comprar los productos para casa, es un submenu
def opcionsub():
    opc=0
    max=5
    while(opc!=max):
        print("#########  SUPERMERCADOS  ###########")
        print("1. METRO")
        print("2. TOTTUS")
        print("3. PRECIO UNO")
        print("4. SUPER ")
        print("5. VOLVER AL MENU INICIAL ")
        print("#####################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,5)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()
        if(opc==4):
            subopcion4()
        print(" ")

#EMenu principal, en el que consiste clasificar los productos y sus precios
opc=0
max=5
while(opc!=max):
    print("================================================")
    print("================================================")
    print("************** INSCRIPCION *********************")
    print("** 1. añadir comprar                         ***")
    print("** 2. mostar compras                         ***")
    print("** 3. mostrar precio y productos por separado **")
    print("** 4. Elegir el supermercado                  **")
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

