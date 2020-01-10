import libreria
def opcion1():
    def opcionA():
        #1. pedir el numero de asiento del pasajero
        #2. pedir el numero de dni
        #3. guardar los datos en "pasaje.txt"
        asiento=libreria.pedir_numero("ingrese el numero de asiento:",1,50)
        dni=libreria.pedir_dni("ingrese el dni: ")
        pasajero=libreria.pedir_nombre("ingrese el nombre del pasajero: ")
        contenido=str(asiento)+" - "+str(dni)+" - "+pasajero+ "\n"
        libreria.agregar_datos("pasaje.txt",contenido,"a")
        print("los datos de su pasaje se guardaron con exito")
    def opcionB():
        #4. acceder al archivo pasaje.txt y mostrar los datos
        print("asiento - dni - pasajero")
        datos=libreria.obtener_datos("pasaje.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("########## PASAJE ##########")
        print("#1. Agregar el datos del asiento, dni y nombre")
        print("#2. Mostrar datos")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir la fecha en que va a viajar
        #2. pedir que ingrese un codigo de viaje
        #3. guardar el contacto en "pasaporte.txt"
        fecha=libreria.pedir_fecha("ingrese la fecha en que va a viajar:")
        codigo=libreria.pedir_clave("ingrese el codigo de viaje(####): ")
        nombre=libreria.pedir_nombre("ingrese el nombre del pasajero: ")
        contenido=fecha+" - "+str(codigo)+" - "+nombre+"\n"
        libreria.agregar_datos("pasaporte.txt",contenido,"a")
        print("los datos del pasajero se guardaron con exito")
    def opcionB():
        #4. acceder al archivo pasaporte.txt y mostrar los datos
        datos=libreria.obtener_datos("pasaporte.txt")
        print("fecha - codigo - nombre")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("######## PASAPORTE #########")
        print("#1. Agregar datos del pasajero")
        print("#2. Mostrar datos del pasajero")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
opc=0
max=3
while(opc!=max):
    print("########## OPCIONES #############")
    print("#1. PASAJE ")
    print("#2. PASAPORTE")
    print("#3. Salir")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
