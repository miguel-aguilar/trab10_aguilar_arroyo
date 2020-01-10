import libreria
def opcion1():
    #1. pedir el  nombre del trabajador
    #2. pedir la ficha de incripcion
    #3. guardar datos en "ficha_trabajo.txt"
    nombre=libreria.pedir_nombre("ingrese el nombre del trabajador: ")
    tipo=libreria.pedir_tipo("ingrese el tipo de trabajador(nombrado,empleado,contratado): ")
    contenido=nombre+" es "+tipo+"\n"
    libreria.agregar_datos("ficha_trabajo.txt",contenido,"a")
    print("inscripcion guardada con exito")
def opcion2():
    #1. acceder al archivo ficha_trabajo.txt y mostrar los datos
    datos=libreria.obtener_datos("ficha_trabajo.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
opc=0
max=3
while(opc!=max):
    print("######### TIPO DE TRABAJADOR ##########")
    print("# 1. Añadir trabajador ")
    print("# 2. Mostrar lista de trabajadores ")
    print("# 3. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
