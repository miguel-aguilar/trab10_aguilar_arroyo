import libreria

def opcionA():
    # 1. Pedir el monbre del alumno
    # 2. Pedir DNI
    # 3. Pedir nacionalidad
    # 4. Guardad datos en el archivo info.txt
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    DNI=libreria.pedir_dni("Ingrese DNI")
    nacionalidad=libreria.pedir_nombre("Ingrese Nacionalidad:")
    contenido=nombre+"===>"+str(DNI)+"===>"+nacionalidad+"\n"
    libreria.agregar_datos("obtener_visa.txt",contenido,"w")
    print("Informacion de la persona guardada")

# Esta opcion ter permitira mostar los datos que contiene este archivo
def mostrarAlumnos():
    archivo=open("obtener_visa.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()

# Esta opcion te clasificara los datos de manera ordenada  y clasificada
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("obtener_visa.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, DNI,nacionalidad = item.split("===>")
            msg="INFORMACION DEL INDIVIDUO :"+"\n"+"NOMBRE : {}"+"\n"+"DNI {}"+"\n"+"NACIONALIDAD {}"
            nombre=nombre.replace("\n","")
            DNI=DNI.replace("\n","")
            nacionalidad=nacionalidad.replace("\n","")
            print(msg.format(nombre, DNI,nacionalidad))
        #fin_for
    else:
        print("No hay datos")

#Este submenu te permite escoger el pais donde quieras ir, y te dara recomendacion hacerca de la documentacion que se debe presentar
def opcionsub():
    opc=0
    max=5
    while(opc!=max):
        print("#########  LISTA DE PAISES  ###########")
        print("##(RECOMENDACION EN PRESENTACION DE DOCUMENTOS)##")
        print("1. INGLETERRA")
        print("2. ALEMANIA")
        print("3. ESTADOS UNIDOS")
        print("4. CHINA ")
        print("5. VOLVER AL MENU INICIAL ")
        print("#####################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,5)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()
        if(opc==4):
            subopcion4()
        print(" ")

# Consejos dependiendo  el lugar escogido
def subopcion1():
    print("*DOCUMENTOS  A PRESENTAR*")
    print("*1_DNI                 **")
    print("*1_PASAPORTE           **")
    print("*1_VISA                **")
    print("*1_ANTECEDENTES PENALES**")
    print("*************************")
def subopcion2():
    print("*DOCUMENTOS  A PRESENTAR*")
    print("*1_DNI                 **")
    print("*1_PASAPORTE           **")
    print("*1_ANTECEDENTES PENALES**")
    print("*************************")
def subopcion3():
    print("*DOCUMENTOS  A PRESENTAR*")
    print("*1_DNI                 **")
    print("*1_VISA                **")
    print("*1_PASAPORTE           **")
    print("*1_REPORTE DE CUENTAS  **")
    print("*1_ANTECEDENTES PENALES**")
    print("*************************")
def subopcion4():
    print("*DOCUMENTOS  A PRESENTAR*")
    print("*1_DNI                 **")
    print("*1_PASAPORTE           **")
    print("*1_ANTECEDENTES PENALES**")
    print("*************************")
#fin_while
print("Fin del MENU")

#MENU PRINCIPAL
# Consiste en optener datos y agregar informacion para poder tener un pasaporte
opc=0
max=5
while (opc != max):
    # 1. Imprecion del menu
    print("#################################################")
    print("###  DATOS PARA OBTENER PASAPORTE             ###")
    print("#################################################")
    print("1. PREGUNTAS DE REGIMEN                         #")
    print("2. DATOS GUARDADOS                              #")
    print("3. INFORMACION CLASIFICADA                      #")
    print("4. SELECCIONE LUGAR DONDE IR (recomendaciones)  #")
    print("5. Salir                                        #")
    print("#################################################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,3)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        mostrarAlumnos()
    if(opc == 3):
        obtener_sum()
    if(opc == 4):
        opcionsub()


    #fin mapeo
