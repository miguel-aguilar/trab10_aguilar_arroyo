import libreria
def opcion1():
    def opcionA():
        #1. pedir el numero de dni del cliente
        #2. pedir el nombre del cliente
        #3. guardar los datos en "datos.txt"
        dni=libreria.pedir_dni("ingrese el numero de dni:")
        cliente=libreria.pedir_nombre("ingrese el nombre del cliente: ")
        contenido=cliente+"-("+str(dni)+")\n"
        libreria.agregar_datos("datos.txt",contenido,"a")
        print("los datos del cliente han sido guardados con exito")
    def opcionB():
        #4. acceder al archivo datos.txt y mostrar los datos
        datos=libreria.obtener_datos("datos.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### DATOS DE BOLETA #######")
        print("#1. agregar datos del cliente")
        print("#2. mostrar datos del cleinte")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el ruc del cliente
        #2. pedir el nombre del cleinte
        #3. guardar los datos en "datos1.txt"
        ruc=libreria.pedir_ruc("ingrese su ruc:")
        nombre=libreria.pedir_nombre("ingrese el nombre del cleinte: ")
        contenido=nombre+"-("+str(celular)+")\n"
        libreria.agregar_datos("datos1.txt",contenido,"a")
        print("los datos del cliente han sido guardado con exito")
    def opcionB():
        #4. acceder al archivo datos1.txt y mostrar los datos
        datos=libreria.obtener_datos("datos1.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### DATOS DE FACTURA ######")
        print("#1. agregar datos del cliente")
        print("#2. mostrar datos del cliente")
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
    print("########## DATOS #############")
    print("#1. POR BOLETA ")
    print("#2. POR FACTURA")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
