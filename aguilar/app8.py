import libreria
def opcion1():
    #1. pedir el nombre de juego solicitado
    #2. pedir el tipo de ps en el que va a jugar
    #3. guardar datos en "juegos.txt"
    juego=libreria.pedir_juego("por favor ingrese el nombre del juego: ")
    ps=libreria.pedir_numero("ingrese el numero de ps que usted tiene(1,2,3,4): ",1,4)
    contenido=juego+" -"+" ps"+str(ps)+"\n"
    libreria.agregar_datos("juegos.txt",contenido,"a")
    print("su juego a sido guardado con exito")
def opcion2():
    #4. acceder al archivo juegos.txt y mostrar los datos
    datos=libreria.obtener_datos("juegos.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo juegos.txt y separar los nombres de los juegos y el tipo de ps por separado
def opcion3():
    sep=libreria.mostrar_separacion("juegos.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## inscripcion ################")
    print("# 1. Agregar juego ")
    print("# 2. Mostrar juegos agregados ")
    print("# 3. Mostrar los juegos y el tipo de ps por separado")
    print("(juegos disponibles: mario,pes)")
    print("# 4. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        opcion3()
print("fin del programa")
