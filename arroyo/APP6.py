
import libreria


def opcionA():
    # 1. Pedir el monbre del alumno
    # 2. Pedir DNI
    # 3. Pedir nacionalidad
    # 4. Guardad datos en el archivo obtener_visa.txt
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    DNI=libreria.pedir_dni("Ingrese DNI")
    nacionalidad=libreria.pedir_nombre("Ingrese Nacionalidad:")
    contenido=nombre+"===>"+str(DNI)+"===>"+nacionalidad+"\n"
    libreria.agregar_datos("obtener_visa.txt",contenido,"w")
    print("Informacion de la persona guardada")

# 2. Mostrar lo que contiene el archivo
def mostrarAlumnos():
    archivo=open("obtener_visa.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()
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

#Interfas de menu,  donde se puede escoger opciones
opc=0
max=4
while (opc != max):
    # 1. Imprecion del menu
    print("#################################")
    print("###  DATOS PARA OBTENER VISA  ###")
    print("#################################")
    print("1. PREGUNTAS DE REGIMEN         #")
    print("2. DATOS GUARDADOS              #")
    print("3. INFORMACION CLASIFICADA      #")
    print("4. Salir                        #")
    print("#################################")
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
