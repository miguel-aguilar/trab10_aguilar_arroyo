import libreria

def agregarIP():
    # 1. Pedir la IP
    hostname=libreria.pedir_nombre("Ingrese el nombre del dispositivo:")
    ip=libreria.pedir_ip("Ingrese el IP:")
    # 2. Guardar la IP en el archivo ip.txt
    contenido=hostname + "-" + ip + "\n"
    libreria.agregar_datos("ip.txt", contenido, "w")
    print("Datos guardados")

def mostrarIP():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("ip.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, ip = item.split("-")
            msg="DESCRIPCION DEL DISPOSITIVO : "+"\n"+"La PC {} "+"\n"+"tiene el IP {} "
            nombre=nombre.replace("\n","")
            ip=ip.replace("\n","")
            print(msg.format(nombre, ip))
        #fin_for
    else:
        print("No hay datos")

#Menu secndario
#consiste en la eleccion del lugar de creacion, en el cual te daran datos curioso dependiendo el lugar donde se
#fabrico el dispositivo
def opcionsub():
    opc=0
    max=5
    while(opc!=max):
        print(" ")
        print("#########  LISTA DE PAISES  ###################")
        print("##(DATOS CURIOSOS ACERCA DEL LUGAR DE CREACION)##")
        print("1. INGLETERRA                                  **")
        print("2. ALEMANIA                                    **")
        print("3. ESTADOS UNIDOS                              **")
        print("4. CHINA                                       **")
        print("5. VOLVER AL MENU INICIAL                      **")
        print("#################################################")
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
#Datos curiosos  sobre el ligar de creacion
def subopcion1():
    print("El dispositivo fue creador por cienticos expectos en la decoficacion de informacion clasificada")
def subopcion2():
    print("Los dispositivos creados por cientificos alemanes, tuvieron su auge en tecnologia en la segunda guerra mundial, y la guerra fria dada despues, ya que competia un pais grande, el cual es estados unidos")
def subopcion3():
    print("Estados siempre ha sido un pais revolucionario en la creacion de dispositivos, el cual cada dia surgen dispositvos que realizan innumerables cosas")
def subopcion4():
    print("China, el principal competencia de estados unidos, en las ultimas decadas esta destacando en la fabricacion de dispositvos electrnico, haciendo mas facil las actividades de las personas")


#Menu principal
#Consiste en la introduccion del IP con datos personasles
opc=""
max=3
while(opc != max):
    print(" ")
    print("################### MENU ##################")
    print("# 1. Agregar IP                           #")
    print("# 2. Mostrar CARACTERISTICAS              #")
    print("# 3. SELECCIONAR ORIGEN DEL DISPOSITIVO   #")
    print("# 4. Salir                                #")
    print("###########################################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarIP()
    if ( opc ==2 ):
        mostrarIP()
    if ( opc ==3 ):
        opcionsub()
#fin_while
