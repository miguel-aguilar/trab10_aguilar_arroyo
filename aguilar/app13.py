import libreria
def opcion1():
    def opcionA():
        #1. pedir el nombre del cumpleañero
        #2. pedir el dia de su cumple
        #3. guardar los datos en "cumpleaños.txt"
        mes=libreria.pedir_mes("ingrese el mes de su cumpleaños(enero,febrero,marzo,abril"
                               "mayo,junio,julio,agosto,septiembre,octubre,noviembre):")
        dia=libreria.pedir_numero("ingrese el dia de su cumpleaños: ", 1,31)
        contenido=mes+"-("+str(dia)+")\n"
        libreria.agregar_datos("cumpleaños.txt",contenido,"a")
        print("los datos se guardaron con exito")
    def opcionB():
        #4. acceder al archivo cumpleaños.txt y mostrar los datos
        datos=libreria.obtener_datos("cumpleaños.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("##### FECHAS DE CUMPLES ######")
        print("#1. agregar el mes y dia del cumpleaños")
        print("#2. mostrar datos de las fechas")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el tamaño del regalo
        #2. pedir el nombre que debe ir escrito
        #3. guardar los datos en "regalos.txt"
        regalos=libreria.pedir_tamano("ingrese el tamaño del regalo(pequeño,mediano,grande):")
        nombre=libreria.pedir_nombre("ingrese el nombre que debe ir escrito: ")
        contenido=regalos+" - ("+str(nombre)+")\n"
        libreria.agregar_datos("regalos.txt",contenido,"a")
        print("los datos de los regalos se ingresaron exito")
    def opcionB():
        #4. acceder al archivo regalos.txt y mostrar los datos
        datos=libreria.obtener_datos("regalos.txt")
        print ("tamaño - (nombre)")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("######### LOS REGALOS #########")
        print("#1. agregar las estructuras de los regalos")
        print("#2. mostrar datos")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
    exit()
opc=0
max=3
while(opc!=max):
    print("########## CUMPLEAÑOS #############")
    print("#1. FECHA ")
    print("#2. REGALOS")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
