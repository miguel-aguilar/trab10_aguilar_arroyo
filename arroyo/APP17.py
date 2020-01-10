import libreria
def nuevoAlumno():
    # 1. Pedir nota1
    # 2. Pedir nota2
    # 3. Pedir nota3
    # 4. Guardad datos en el archivo "registro_notas.txt"
    nota1=libreria.pedir_nota("ingrese nota 1: ")
    nota2=libreria.pedir_nota("ingrese nota 2: ")
    nota3=libreria.pedir_nota("ingrese nota 3: ")
    contenido=str(nota1)+"===>"+str(nota2)+"===>"+str(nota3)+"\n"
    libreria.agregar_datos("registro_notas.txt",contenido,"a")
    print("Informacion de la persona guardada")

#Esta funcion te permitira mostar los datos ingresados a la carpte registro_notas
def mostrarAlumnos():
    archivo=open("registro_notas.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()


def obtener_sum():
    # 1. Abrir el archivo "registro_notas.txt" y mostrar sus datos
    data=libreria.obtener_datos_lista("registro_notas.txt")

    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nota1, nota2,nota3 = item.split("===>")
            promedio=(int(nota1)+int(nota2)+int(nota3))/3
            msg="NOTA1 :"+str(nota1)+"\n"+ "NOTA2 :"+str(nota2)+"\n"+"NOTA3 :"+str(nota3)+"\n"+"PROMEDIO:"+str(promedio)

            print(msg)
        #fin_for
    else:
        print("No hay datos")

#SUBMENU
#Consiste en elegir el intevalo de nota en el te encuentras y te reportara un mensaje enviado por el profesor
def opcionsub():
    opc=0
    max=4
    while(opc!=max):
        print("######## INTERFASE DE INFORMACION  #########")
        print("##(Seleccionar opcion)##")
        print("1. PROMEDIO<10")
        print("2. PROMEDIO>11")
        print("3. PROMEDIO>15")
        print("4. VOLVER AL MENU INICIAL ")
        print("#####################################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,4)
        if(opc==1):
            subopcion1()
        if(opc==2):
            subopcion2()
        if(opc==3):
            subopcion3()
        print(" ")

#Esta opcion son los mensajes que entrega el profesor a los alumnos, dependiendo la nota de alumno
def subopcion1():
    print("*PROMEDIO<10*")
    print("*Si quieren por lo menos aprobar el curso hacer las siguientes actividades **")
    print("********* ACTIVIDADES ********")
    print("*150  ejercicios resueltos  **")
    print("*Presentacion de cuaderno   **")
    print("*Exposicion de 5 ejercicios  *")
    print("******************************")
def subopcion2():
    print("*PROMEDIO>11*")
    print("*Si quieren levantar su nota presentar las siguientes actividades **")
    print("********* ACTIVIDADES ********")
    print("*1_75 ejerccios             **")
    print("*1_Presentacion de cuaderno **")
    print("*******************************")
def subopcion3():
    print("*PROMEDIO>15*")
    print("*Felicidades alumno, su nota es aprobatoria **")
    print("********* ACTIVIDADES ********")
    print("*1---------------------**")
    print("*1---------------------**")
    print("*1---------------------**")
    print("*1---------------------**")
    print("*1---------------------**")
    print("*************************")

#fin_while
print("Fin del MENU")


#MENU PRINCIPPAL
#Consiste en el ingreso de notas del curso de programacion y  sacar el promedio
opc=0
max=5
while (opc != max):
    print("#######  REGISTRO DE NOTAS DE PROGRAMACION   #######")
    print("#1. REDACTAR NOTAS:      #")
    print("#2. MOSTAR NOTAS:   #")
    print("#3. MOSTRAR PROMEDIO:   #")
    print("#4. RECOMENDACIONES A CERCA DE SU PROMEDIO:   #")
    print("#5. salir              #")
    print("########################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,4)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        mostrarAlumnos()
    if (opc == 4):
        opcionsub()
#fin_menu

