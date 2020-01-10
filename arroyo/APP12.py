import libreria
# 1. Pedir el nombre del alumno
def subopcionA():
    print("INGRESE el ID DEL PLAYER 1")
    nombre=libreria.pedir_nombre("Ingrese Nombre:")
    # 1. Pedir el nombre del alumno
    contenido=nombre+"\n"
    libreria.agregar_datos("LISTAJUGADORES.txt",contenido,"w")
    print("SI DESEA JUGAR INGRESE DOS CONINS")
    # 1. Elegor una opccion, dmas dons opciones
    opc=0
    max=2
    while(opc!=max):
        opc=libreria.pedir_entero_positivo("Ingrese COINS: ")
    print("################ MENU ################")
    print("******* EL JUEGO ESTA DISPONIBLE******")
    print("#####################################")
    if(opc==max):
        opc=0
        max=1
        print("Si desea regresar al menu  ingrese el numero 1")
        opc=libreria.pedir_entero_positivo("Introducir opcion")
        while(opc!=max):
            opc=libreria.pedir_entero_positivo("opcion incorecta--vuelva a introducir")
        print("########### GRACIAS POR JUGAR ###########")



def mostrarAlumnos():
    print("ID DE JUGADORES")
    archivo=open("LISTAJUGADORES.txt")
    datos=archivo.read()
    print(datos)
    archivo.close()


def subopcionC():
    print("########## MODO DE JUEGO  ##############")
    print("1. ARCADE")
    print("2. AVENTURA")
    print("3. DIFICIL")
    print("4. Exit")
    print("#####################################")


def opcionA():
    opc=0
    max=3
    while(opc!=max):
        print("################ MENU ################")
        print("1. Player 1")
        print("2. mode")
        print("3. Exit")
        print("#####################################")
        opc=libreria.pedir_entero_positivo("Ingrese opcion: ")
        if(opc==1):
            subopcionA()
        if(opc==2):
            subopcionC()
    print("USTED HA SALIDO DEL JUEGO, TENDRA NUEVOS JUEGOS QUE DISFRUTAR")
    print(" ")

def opcionB():
    opc=0
    max=3
    while(opc!=max):
        print("################ MENU ################")
        print("1. Player 1")
        print("2. mode")
        print("3. Exit")
        print("#####################################")
        opc=libreria.pedir_entero_positivo("Ingrese opcion: ")
        if(opc==1):
            subopcionA()
        if(opc==2):
            subopcionC()
        print("USTED HA SALIDO DEL JUEGO, TENDRA NUEVOS JUEGOS QUE DISFRUTAR")
        print(" ")

def opcionC():
    opc=0
    max=3
    while(opc!=max):
        print("################ MENU ################")
        print("1. Player 1")
        print("2. mode")
        print("3. Exit")
        print("#####################################")
        opc=libreria.pedir_entero_positivo("Ingrese opcion: ")
        if(opc==1):
            subopcionA()
        if(opc==2):
            subopcionC()
        print("USTED HA SALIDO DEL JUEGO, TENDRA NUEVOS JUEGOS QUE DISFRUTAR")
        print(" ")
def opcionD():
    opc=0
    max=3
    while(opc!=max):
        print("################ MENU ################")
        print("1. Player 1")
        print("2. mode")
        print("3. Exit")
        print("#####################################")
        opc=libreria.pedir_entero_positivo("Ingrese opcion: ")
        if(opc==1):
            subopcionA()
        if(opc==2):
            subopcionC()
        print("USTED HA SALIDO DEL JUEGO, TENDRA NUEVOS JUEGOS QUE DISFRUTAR")
        print(" ")

opc=0
max=6
while(opc!=max):
    print("################ MENU ################")
    print("1. Donkey Kong")
    print("2. Mario Bros")
    print("3. Spece Invaders")
    print("4. contra")
    print("5. MOTRAR ID JUGADORES")
    print("6. Salir")
    print("######################################")
    opc=libreria.pedir_entero_positivo("Ingrese opcion: ")
    if(opc==1):
        opcionA()
    if(opc==2):
        opcionB()
    if(opc==3):
        opcionA()
    if(opc==4):
        opcionD()
    if(opc==5):
        mostrarAlumnos()

print(" ")
print("######################################")
print("GRACIAS, POR SU PREFERENCIA")
print("VUELVA PRONTO")
print("######################################")
