import libreria
def nuevoAlumno():
    # 1. Pedir el monbre del alumno
    # 2. Pedir edad
    # 3. Guardad datos en el archivo info.txt
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    edad=libreria.pedir_nombre("Ingrese la direecion de su domicilio")
    contenido=nombre+"===>"+edad+"\n"
    libreria.agregar_datos("empadronamiento.txt",contenido,"w")
    print("Informacion de la persona guardada")

#esta opcion nos permite ingresar al archivo "empadronamiento.txt" y revisar lo que contiene
def mostrarAlumnos():
    archivo=open("empadronamiento.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()
#esta opcion nos permite ingresar al archivo "empadronamiento.txt" y revisar lo que contiene y clasificarlo ordenadamente
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

#este conjunto de opciones nos dara un mensaje de recomendacion segun nuestra condicion ingresada
def subopcion1():
    print("Usted no requiere ayuda economica del estado")
def subopcion2():
    print("Usted puedeen algun momento solicitar ayuda")
def subopcion3():
    print("USted necesita acesoria sobre el manejo de dinero")
    print("*******************")
    print("**NUMERO A LLAMAR **")
    print("**Numero: 989765522")
    print("**Numero: 934761022")
    print("***********************************")
def subopcion4():
    print("Necesita ayuda inmediatamente")
    print("**NUMERO A MINISTRO DE LA MUJER**")
    print("**Numero:+51 902165522")
    print("**Numero:+51 952741022")
    print("***********************************")

#Esta interfast te perminte pedir el nivel de condicion en el que te encuentras
def opcionsub():
    opc=0
    max=5
    while(opc!=max):
        print("#########  CONDICION ECONOMICA  ###########")
        print("1. CLASE MEDIA")
        print("2. NO POBRE")
        print("3. POBRE")
        print("4. POBRE EXTREMO ")
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

#El menu principal
opc=0
max=5
while (opc != max):
    print(" ")
    print("#######################################")
    print("#######  INFORMACION PERSONAL   #######")
    print("#1. Registrar Nueva Persona:          #")
    print("#2. Recopilacion de datos:            #")
    print("#3. Datos ordenados:                  #")
    print("#4. Seleccione su condicion economica:#")
    print("#5. salir                             #")
    print("#######################################")
    print("#######################################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,3)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        obtener_sum()
    if (opc == 4):
        opcionsub()
#fin_menu
