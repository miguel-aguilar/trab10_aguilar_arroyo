import libreria

def agregarIP():
    # 1. Pedir la IP
    # 1. Pedir la oriegn del dispoditivo
    hostname=libreria.pedir_nombre("Ingrese el nombre del dispositivo:")
    ip=libreria.pedir_ip("Ingrese el IP:")
    origen=libreria.pedir_nombre("Ingrese el origen del dispositivo")
    # 2. Guardar la IP en el archivo ip.txt
    contenido=hostname + "-" + ip +"-"+origen+ "\n"
    libreria.agregar_datos("ip.txt", contenido, "w")
    print("Datos guardados")

def mostrarIP():
    # 1. Abrir el archivo ip.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("ip.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            nombre, ip,origen = item.split("-")
            msg="DESCRIPCION DEL DISPOSITIVO : "+"\n"+"La PC {} "+"\n"+"tiene el IP {} "+"\n"+ "origen: {} "
            nombre=nombre.replace("\n","")
            ip=ip.replace("\n","")
            origen=origen.replace("\n","")
            print(msg.format(nombre, ip,origen))
        #fin_for
    else:
        print("No hay datos")

#se muestra la interfas de esta funcion el cual es, identificar un IP
opc=""
max=3
while(opc != max):
    print("######### MENU ################")
    print("# 1. Agregar IP               #")
    print("# 2. Mostrar CARACTERISTICAS  #")
    print("# 3. Salir                    #")
    print("###############################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarIP()
    if ( opc ==2 ):
        mostrarIP()
#fin_while

