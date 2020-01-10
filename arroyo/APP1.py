import libreria
def opcion1():
#pedir el roducto
#pedir la ficha compras
#guardar datos en compras.txt
    producto=libreria.pedir_nombre("Ingrese el producto")
    costo=libreria.pedir_entero_positivo("ingrese el costo del producto")
    contenido=producto+"-"+str(costo)+"\n"
    libreria.agregar_datos("compras.txt",contenido,"w")
    print("Su compra se guardo con exito")
#Obtener los datos
def opcion2():
    datos=libreria.obtener_datos("compras.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #Obtener los parametros
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

#Mostrar  las opciones por seprado,
opc=0
max=4
while(opc!=max):
    print("********* INSCRIPCION **************")
    print("** 1. añadir comprar")
    print("** 2. mostar compras")
    print("** 3. mostrar precio y productos por separado")
    print("** 4. salir")
    opc=libreria.pedir_entero("ingrese opcion:",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        obtener_sum()






