import libreria

def opcionA():
    # 1. Pedir el nombre
    # 2. Pedir DNI
    # 3. Pedir telefono
    # 3. Guardad datos en el archivo "datos_personales.txt"
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    DNI=libreria.pedir_dni("Ingrese DNI")
    telefono=libreria.pedir_telefono("Ingrese numero de telefono:")
    contenido=nombre+"===>"+str(DNI)+"===>"+str(telefono)+"\n"
    libreria.agregar_datos("datos_personales.txt",contenido,"w")
    print("Informacion de la persona guardada")

#esta opcion te permite mostar los datos introducidos a la carpeta datos_personales,txt
def mostrarAlumnos():
    archivo=open("datos_personales.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()

def obtener_sum():
    # 1. Abrir el archivo "datos_personales.txt" y mostrar sus datos ordenados
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

#SUB MENU
#Consiste en mostar los cursos que llevaresmos en los tres primeros ciclos, por separado
def opcionsub():
    opc=0
    max=4
    while(opc!=max):
        print("######## CURSOS A LLEVAR EN LOS 3 CICLOS #########")
        print("1. CICLO I")
        print("2. CICLO II")
        print("3. CICLO III")
        print("4.Salir")
        print("#####################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,4)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()
        print(" ")

#SUBMENUS
#Esta sopciones muestran el contenido de cada opcion elegido en el Submenu principal
def subopcion1():

    print("*** CURSOS DEL PRIMER CICLO ***")
    print("*-PROGRAMACION")
    print("*-QUIMICA")
    print("*-TECNICAS DE ESTUDIO")
    print("*-MATEMATICA BASICA")
    print("******************************")
def subopcion2():

    print("*****SEGUNDO CICLO ******")
    print("*-PROGRAMACION II")
    print("*-ANALISIS MATEMATICO II")
    print("*-INTRODUCCION A LA INGIENIERIA ELECTRONICA")
    print("*-MATEMATICA BASICA II")
    print("*******************************")
def subopcion3():

    print("***** TERCER CICLO *****")
    print("*-PROGRAMACION III")
    print("*-CIRCUITOS")
    print("*-FISICA I")
    print("*************************")

#fin_while
print("Fin del MENU")

#MENU PRINCIPAL
#Consiste es introducir una base de datos del estudiante y hay una opcion agregada donde te informa los cursos que llevaras en los siguiente ciclos
opc=0
max=5
while (opc != max):
    # 1. Imprecion del menu
    print("############################################")
    print("###  INFORMACION PRIVADA DEL ESTUDIANTE  ###")
    print("############################################")
    print("1. PREGUNTAS DE INGRESO                    #")
    print("2. DATOS GUARDADOS                         #")
    print("3. INFORMACION CLASIFICADA                 #")
    print("4. OTRAS OPCIONES                          #")
    print("5. Salir                                   #")
    print("############################################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,5)

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


#fin_while
print("Fin del MENU")
