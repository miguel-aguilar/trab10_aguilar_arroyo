import libreria
def opcion1():
    #1. pedir el producto
    #2. pedir la ficha compras
    #3. guardar datos en "compras.txt"
    producto=libreria.pedir_nombre("ingrese el producto: ")
    costo=libreria.pedir_real("ingrese el costo del producto: ")
    contenido=producto+"-"+str(costo)+"\n"
    libreria.agregar_datos("compras.txt",contenido,"a")
    print("su compra se guardo con exito")
def opcion2():
    #4. acceder al archivo compras.txt y mostrar los datos
    datos=libreria.obtener_datos("compras.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo compra.txts y separar los precios y productos
def opcion3():
    sep=libreria.mostrar_separacion("compras.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## inscripcion ################")
    print("# 1. añadir compra ")
    print("# 2. mostrar compras ")
    print("# 3. mostrar precios y productos porseparado")
    print("# 4. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        opcion3()
print("fin del programa")
