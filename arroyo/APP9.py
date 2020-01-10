import libreria
def nuevoAlumno():
    # 1. Pedir el monbre del alumno
    # 2. Pedir apellido
    # 3. Guardad datos en el archivo "matricula.txt"
    nombre=libreria.pedir_nombre("Ingrese su nombre")
    apellido=libreria.pedir_nombre("ingrese su apellido: ")
    nunr_credito=libreria.pedir_nota("ingrese el numero de creditos que posee ")
    contenido=nombre+"===>"+apellido+"===>"+str(nunr_credito)+"\n"
    libreria.agregar_datos("matricula.txt",contenido,"w")
    print("Informacion de la persona guardada")


def mostrarAlumnos():
    archivo=open("matricula.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()

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


opc=0
max=4
while (opc != max):
    print(" ")
    print("#######  REGISTRO DE NOTAS DE PROGRAMACION   #######")
    print("#1. DATOS PERSONALES:                              #")
    print("#2. MOSTRAR APUNTES:                               #")
    print("#3. INFORMACION IMPORTANTE:                        #")
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
