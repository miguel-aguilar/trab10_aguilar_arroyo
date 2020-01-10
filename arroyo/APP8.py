import libreria
def nuevoAlumno():
    # 1. Pedir nota1
    # 1. Pedir nota2
    # 1. Pedir nota3
    # 1. Pedir nota4
    # 3. Guardad datos en el archivo "registro_notas.txt",
    nota1=libreria.pedir_nota("ingrese nota PROGRAMACION: ")
    nota2=libreria.pedir_nota("ingrese nota MATEMATICA BASICA: ")
    nota3=libreria.pedir_nota("ingrese nota QUIMICA: ")
    nota4=libreria.pedir_nota("ingrese nota ANALISIS MATEMATICO: ")
    contenido=str(nota1)+"===>"+str(nota2)+"===>"+str(nota3) +"===>"+str(nota4) +"\n"
    libreria.agregar_datos("registro_notas.txt",contenido,"w")
    print("Informacion de la persona guardada")

# 2. Se mostrara los datos que contenga el archivo "registro_notas.txt"
def mostrarAlumnos():
    archivo=open("registro_notas.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()

# 2. LOs datos registrados en el archivo "registro_notas.txt" , seran ordenados y clasificados
def obtener_sum():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("registro_notas.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nota1, nota2,nota3,nota4 = item.split("===>")
            promedio=(int(nota1)+int(nota2)+int(nota3)+int(nota4))/3
            msg="NOTA DE PROGRAMACION :"+str(nota1)+"\n"+ "NOTA DE MATEMATICA BASICA :"+str(nota2)+"\n"+"NOTA DE QUIMICA :"+str(nota3)+"\n"+"NOTA DE ANALISIS MATEMATICO :"+str(nota4)+"\n"+"PROMEDIO:"+str(promedio)

            print(msg)
        #fin_for
    else:
        print("No hay datos")

# 2. Interfase de menu de NOTAS DE CURSOS DE FIN DE CICLO
opc=0
max=4
while (opc != max):
    print(" ")
    print("#######  NOTAS DE CURSOS DE FIN DE CICLO  #######")
    print("#1. REDACTAR NOTAS POR CURSOS:                  #")
    print("#2. MOSTAR NOTAS:                               #")
    print("#3. MOSTRAR PROMEDIO:                           #")
    print("#4. salir                                       #")
    print("#################################################")

    opc=libreria.pedir_entero("Ingrese opcion:",1,4)

    if (opc == 1):
        nuevoAlumno()
    if (opc == 2):
        mostrarAlumnos()
    if (opc == 3):
        obtener_sum()
#fin_menu
