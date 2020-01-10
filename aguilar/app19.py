import libreria
def opcion1():
    def opcionA():
        #1. pedir el peso con el que inicio
        #2. pedir el peso despues de a ver pasado un año
        #3. guardar los datos en "peso.txt"
        peso1=libreria.pedir_real("ingrese el peso con el que inicio el año:")
        peso2=libreria.pedir_real("ingrese el peso con el que finalizo el año: ")
        contenido=str(peso1)+"-"+str(peso2)+"\n"
        libreria.agregar_datos("peso.txt",contenido,"a")
        print("tus pesos se han guardado exitosamente")
    def opcionB():
        #4. acceder al archivo peso.txt y ver la variacion de tu peso
        print("OJO: Si es que la opcion (bajó) esta con negativo entonces quiere decir que subiste de peso")
        print("(antes) - (despues) - (bajó(kg.))")
        datos=libreria.obtener_datos_lista("peso.txt")
        for linea in datos:
            linea = linea.replace("\n", "")
            pes1, pes2 = linea.split("-")
            sum=libreria.sumar(pes1,pes2)
            print("("+str(pes1) + ") - (" + str(pes2) + ") - (" + str(sum)+")")
    opc=0
    max=3
    while(opc!=max):
        print("############ PESOS ###########")
        print("#1. AGREGAR PESOS ")
        print("#2. MOSTRAR RESULTADOS")
        print("#3. SALIR")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir la talla con la que inició
        #2. pedir la talla despues de a ver pasado un año
        #3. guardar los datos en "talla.txt"
        talla1=libreria.pedir_real("ingrese la talla con la que inicio el año:")
        talla2=libreria.pedir_real("ingrese la talla con la finalizo el año: ")
        contenido=str(talla1)+"-"+str(talla2)+"\n"
        libreria.agregar_datos("talla.txt",contenido,"a")
        print("tus tallas se guardadon exitosamente")
    def opcionB():
        #4. acceder al archivo talla.txt y ver cuanto creciste
        print("(antes) - (despues) - (subio (cm.))")
        datos=libreria.obtener_datos_lista("talla.txt")
        for linea in datos:
            linea = linea.replace("\n", "")
            tal1, tal2 = linea.split("-")
            sum=libreria.sumar(tal1,tal2)
            print("("+str(tal1) + ") - (" + str(tal2) + ") - (" + str(sum)+")")
    opc=0
    max=3
    while(opc!=max):
        print("############ TALLA ###########")
        print("#1. AGREGAR TALLAS ")
        print("#2. MOSTRAR RESULTADOS")
        print("#3. SALIR")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
opc=0
max=3
while(opc!=max):
    print("########## PROGRESOS #############")
    print("#1. PESOS")
    print("#2. TALLAS")
    print("#3. SALIR")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
