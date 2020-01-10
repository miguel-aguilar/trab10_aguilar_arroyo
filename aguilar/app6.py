import libreria
def opcion1():
    #1. pedir el nombre del cliente
    #2. pedir el numero de ruc
    #3. guardar datos en "factura.txt"
    nombres=libreria.pedir_nombre("ingrese su nombre: ")
    ruc=libreria.pedir_ruc("ingrese su ruc: ")
    contenido=nombres+"-"+str(ruc)+"\n"
    libreria.agregar_datos("factura.txt",contenido,"a")
    print("sus datos se guardaron con exito")
def opcion2():
    #4. acceder al archivo factura.txt y mostrar los datos
    datos=libreria.obtener_datos("factura.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo factura.txt y mostrar los nombres y el ruc por separado
def opcion3():
    sep=libreria.mostrar_separacion("factura.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## inscripcion ################")
    print("# 1. añadir datos para la factura ")
    print("# 2. mostrar datos agregados ")
    print("# 3. mostrar nombres y el ruc por separado")
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
