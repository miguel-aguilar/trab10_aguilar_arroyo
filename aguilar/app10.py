import libreria
def opcion1():
    #1. pedir nombres
    #2. pedir el numero de su tarjeta
    #3. pedir la clave de la tarjeta
    #4. guardar datos en "credito.txt"
    nombre=libreria.pedir_nombre("ingrese su nombre: ")
    tarjeta=libreria.pedir_tar("ingrese su numero de tarjeta (**** **** **** ****): ")
    clave=libreria.pedir_clave("ingrese su clave (****): ")
    contenido=nombre+"-"+tarjeta+"-"+str(clave)+"\n"
    libreria.agregar_datos("credito.txt",contenido,"a")
    print("SU CREDITO HA SIDO AGREGADO CON EXITO")
def opcion2():
    #4. acceder al archivo credito.txt y mostrar los datos
    datos=libreria.obtener_datos("credito.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo credito.txt y separar los ciclos de los numeros de dni
def opcion3():
    sep=libreria.mostrar_separacion2("credito.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## CREDITO ################")
    print("# 1. Agregar datos crediticios ")
    print("# 2. Mostrar datos crediticios ")
    print("# 3. Mostrar nombre, el numero de la tarjeta y la clave por separado")
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
