import libreria
def opcion1():
    #1. pedir el  nombre del alumno
    #2. pedir la ficha de incripcion
    #3. guardar datos en "inscripcion.txt"
    nombre=libreria.pedir_nombre("ingrese el nombre: ")
    fecha=libreria.pedir_fecha("ingrese la fecha de suscripcion: ")
    contenido=nombre+"("+fecha+")\n"
    libreria.agregar_datos("inscripcion.txt",contenido,"a")
    print("inscripcion guardada con exito")
def opcion2():
    #1. acceder al archivo inscripcion.txt y mostrar los datos
    datos=libreria.obtener_datos("inscripcion.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
opc=0
max=3
while(opc!=max):
    print("########## INSCRIPCION ################")
    print("# 1. añadir inscripcion ")
    print("# 2. mostrar inscripcion ")
    print("# 3. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
