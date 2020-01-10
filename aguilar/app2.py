import libreria
def opcion1():
    #1. pedir el  nombre de la mascota
    #2. pedir la ficha de mascotas
    #3. guardar datos en "mascotas.txt"
    nombre=libreria.pedir_nombre("ingrese el nombre de tu mascota: ")
    tamano=libreria.pedir_tamano("ingrese el tamaño de tu mascota(grande,mediano,pequeño): ")
    contenido="se agrego a un nuevo miembro y su nombre es '"+nombre+"' de tamano '"+tamano+"'\n"
    libreria.agregar_datos("mascotas.txt",contenido,"a")
    print("los datos de tu mascotas se agrego con exito")
def opcion2():
    #1. acceder al archivo mascotas.txt y mostrar los datos
    datos=libreria.obtener_datos("mascotas.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
opc=0
max=3
while(opc!=max):
    print("########## MASCOTAS ################")
    print("# 1. añadir tu mascota ")
    print("# 2. mostrar lsita de mascotas ")
    print("# 3. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
