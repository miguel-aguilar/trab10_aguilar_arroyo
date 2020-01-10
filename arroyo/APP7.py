import libreria
def nuevoAlumno():
    # 1. Pedir el monbre del alumno
    # 2. Pedir edad
    # 3. Guardad datos en el archivo "registro_notas.txt"
    nota1=libreria.pedir_nota("ingrese nota 1: ")
    nota2=libreria.pedir_nota("ingrese nota 2: ")
    nota3=libreria.pedir_nota("ingrese nota 3: ")
    contenido=str(nota1)+"===>"+str(nota2)+"===>"+str(nota3)+"\n"
    libreria.agregar_datos("registro_notas.txt",contenido,"w")
    print("Informacion de la persona guardada")

# 2. Mostrar lo que contiene el archivo "registro_notas.txt"
def mostrarAlumnos():
    archivo=open("registro_notas.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()


def obtener_sum():
    # 1. Abrir el archivo registro_notas.txt" y mostrar sus datos
    data=libreria.obtener_datos_lista("registro_notas.txt")

    # 2. Comprobar si hay datos
    if ( data != ""):
        for item in data:
            nota1, nota2,nota3 = item.split("===>")
            promedio=(int(nota1)+int(nota2)+int(nota3))/3
            msg="NOTA1 :"+str(nota1)+"\n"+ "NOTA2 :"+str(nota2)+"\n"+"NOTA3 :"+str(nota3)+"\n"+"PROMEDIO:"+str(promedio)

            print(msg)
        #fin_for
    else:
        print("No hay datos")

# Interfasde registro de notas de programacion
opc=0
max=4
while (opc != max):
    print(" ")
    print("#######  REGISTRO DE NOTAS DE PROGRAMACION   #######")
    print("#1. REDACTAR NOTAS:                                #")
    print("#2. MOSTAR NOTAS:                                  #")
    print("#3. MOSTRAR PROMEDIO:                              #")
    print("#4. salir                                          #")
    print("####################################################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,4)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        obtener_sum()
#fin_menu
