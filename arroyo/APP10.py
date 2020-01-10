import libreria

def opcionA():
    # 1. Pedir el monbre del alumno
    # 2. Pedir DNI
    # 2. Pedir telefono
    # 3. Guardad datos en el archivo "datos_personales.txt"
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    DNI=libreria.pedir_dni("Ingrese DNI")
    telefono=libreria.pedir_telefono("Ingrese numero de telefono:")
    contenido=nombre+"===>"+str(DNI)+"===>"+str(telefono)+"\n"
    libreria.agregar_datos("datos_personales.txt",contenido,"w")
    print("Informacion de la persona guardada")

# 3. Se mostrara los archivos ingresados en la carpeta "datos_personales.txt"
def mostrarAlumnos():
    archivo=open("datos_personales.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()

# 3. Se mostrara los archivos ingresados en la carpeta "datos_personales.txt" y sera clasificado y ordenado
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("datos_personales.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, DNI,telefono = item.split("===>")
            msg="INFORMACION DEL INDIVIDUO :"+"\n"+"NOMBRE : {}"+"\n"+"DNI {}"+"\n"+"NUMERO DE CELULAR {}"
            nombre=nombre.replace("\n","")
            DNI=DNI.replace("\n","")
            telefono=telefono.replace("\n","")
            print(msg.format(nombre, DNI,telefono))
        #fin_for
    else:
            print("No hay datos")


opc=0
max=4
# Interfase rel registro de notas de unestudiante
while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###  INFORMACION PRIVADA DEL ESTUDIANTE  ######")
    print("###############################################")
    print("1. PREGUNTAS DE INGRESO                       #")
    print("2. DATOS GUARDADOS                            #")
    print("3. INFORMACION CLASIFICADA                    #")
    print("4. Salir                                      #")
    print("###############################################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,3)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        mostrarAlumnos()
    if(opc == 3):
        obtener_sum()

    #fin mapeo


#fin_while
print("Fin del MENU")
