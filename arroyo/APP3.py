import libreria
def nuevoAlumno():
    # 1. Pedir el monbre del alumno
    # 2. Pedir edad
    # 3. Guardad datos en el archivo info.txt
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    edad=libreria.pedir_nombre("Ingrese la direecion de su domicilio: ")
    contenido=nombre+"===>"+edad+"\n"
    libreria.agregar_datos("empadronamiento.txt",contenido,"w")
    print("Informacion de la persona guardada")

# 1. mostrar el archivo mediante una carpeta txt.o
def mostrarAlumnos():
    archivo=open("empadronamiento.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("empadronamiento.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, domicilio = item.split("===>")
            msg="El senor(a) cuyo nombre es  {} , vive en el domicilio {}"
            nombre=nombre.replace("\n","")
            domicilio=domicilio.replace("\n","")
            print(msg.format(domicilio, domicilio))
        #fin_for
    else:
        print("No hay datos")


opc=0
max=4
while (opc != max):
    print("#######  INFORMACION PERSONAL   #######")
    print("#1. Registrar Nueva Persona:          #")
    print("#2. Recopilacion de datos:            #")
    print("#3. Datos ordenados:                  #")
    print("#4. salir                             #")
    print("########################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,3)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        obtener_sum()
#fin_menu




