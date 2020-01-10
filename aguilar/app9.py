import libreria
def opcion1():
    #1. pedir nombres
    #2. pedir el ciclo universitario
    #3. pedir el numero de dni
    #4. guardar datos en "proyecto.txt"
    nombre=libreria.pedir_nombre("ingrese su nombre: ")
    ciclo=libreria.pedir_ciclo("ingrese el ciclo universitario en el que esta(primero,"
                                "segundo,tercero,cuarto,quinto,sexto,septimo,octavo"
                                "noveno,decimo): ")
    dni=libreria.pedir_dni("ingrese su numero de dni: ")
    contenido=nombre+"-"+ciclo+"-"+str(dni)+"\n"
    libreria.agregar_datos("proyecto.txt",contenido,"a")
    print("TE HAS SUSCRITO CON EXITO")
def opcion2():
    #4. acceder al archivo proyecto.txt y mostrar los datos
    datos=libreria.obtener_datos("proyecto.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo proyecto.txt y separar los ciclos de los numeros de dni
def opcion3():
    sep=libreria.mostrar_separacion2("proyecto.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## SUSCRIPCION ################")
    print("###### GRAN PROYECTO ELECTRONICO ######")
    print("# 1. Suscribirme ")
    print("# 2. Mostrar suscripcion ")
    print("# 3. Mostrar nombre, el ciclo y el numero de dni por separado")
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
