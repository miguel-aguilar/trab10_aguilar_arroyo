import libreria
def nuevoAlumno():
    # 1. Pedir el nombre del alumno
    # 2. Pedir el apellido
    # 3. Pedir el numero de creditos
    # 4. Guardad datos en el archivo "matricula.txt"
    nombre=libreria.pedir_nombre("Ingrese su nombre")
    apellido=libreria.pedir_nombre("ingrese su apellido: ")
    nunr_credito=libreria.pedir_nota("ingrese el numero de creditos que posee ")
    contenido=nombre+"===>"+apellido+"===>"+str(nunr_credito)+"\n"
    libreria.agregar_datos("matricula.txt",contenido,"w")
    print("Informacion de la persona guardada")

#Esta opcion te permite mostar losdatos ingresados
def mostrarAlumnos():
    archivo=open("matricula.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()
#Esta opcion ter permite mejorar la clasificacion de datos introducidos  al archivo matricula.txt
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("matricula.txt")

    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, apellido,nr_credito = item.split("===>")
            costo_matricula=(int(nr_credito)*2)
            msg="NOMBRE :"+nombre+"\n"+ "APELLIDO :"+apellido+"\n"+"NUMERO DE CREDITOS :"+str(nr_credito)+"\n"+"COSTO MATRICULA:"+str(costo_matricula)
            print(msg)
        #fin_for
    else:
        print("No hay datos")

#SUB MENU
#Consiste en mostrar actividades de la universidad, donde quiza algunas de ellas sea importante para mi
def opcionsub():
    opc=0
    max=4
    while(opc!=max):
        print(" ")
        print("##############################################")
        print("######## NOVEDADES DE LA UNIVERSIDAD #########")
        print("1. INICIO DE CICLO                       #####")
        print("2. EXAMEN DE ADMISION                    #####")
        print("3. CICLO DE VERANO                       #####")
        print("4. VOLVER AL MENU INICIAL                #####")
        print("##############################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,4)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()
        print(" ")

#SUBMENUS
#Te muestra los diferentes mensajes de cada opcion
def subopcion1():

    print("********* INICIO DE CICLO ********")
    print("* 17/04/2020  **")
    print("*Comienzan las clases  *")
    print("******************************")
def subopcion2():

    print("***** EXAMEN DE ADMISION ******")
    print("*FECHA: 21/07/2020          **")
    print("*Hbra pocas vacantes*")
    print("*******************************")
def subopcion3():

    print("***** CICLO DE VERANO *****")
    print("*1---------------------**")
    print("*1----01/02/2020   ----**")
    print("*1DURACION: 2 meses**")
    print("*************************")

#fin_while
print("Fin del MENU")

#MENU PRINCIPAL
#Consiste introducir datos personasles para poder obtener mi matricula
opc=0
max=5
while (opc != max):
    print(" ")
    print("####################################")
    print("########## MATRICULA ###############")
    print("#1.  REGISTRO MATRICULA  ###########")
    print("#2. MOSTRAR APUNTES:             ###")
    print("#3. INFORMACION IMPORTANTE:       ##")
    print("#4 : NOVEDADES DE LA UNIVERSIDAD   #")
    print("#5. salir                          #")
    print("####################################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,5)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        obtener_sum()
    if (opc == 4):
        opcionsub()
#fin_menu
