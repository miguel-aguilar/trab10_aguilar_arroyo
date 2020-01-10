import libreria
def opcion1():
    def opcionA():
        #1. pedir la placa del auto
        #2. pedir el color del auto
        #3. guardar los datos en "auto.txt"
        placa=libreria.pedir_placa("ingrese la placa de su auto:")
        color=libreria.pedir_color("ingrese el color del auto(): ")
        contenido=color+" - "+placa+"\n"
        libreria.agregar_datos("auto.txt",contenido,"a")
        print("los datos del auto han sido guardado")
    def opcionB():
        #4. acceder al archivo auto.txt y mostrar los datos
        print("color - placa")
        datos=libreria.obtener_datos("auto.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### AUTO #######")
        print("#1. AGREGAR DATOS DEL AUTO ")
        print("#2. MOSTRAR DATOS DEL AUTO")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el nombre del conductor
        #2. pedir el estado en que ha estado manejando
        #3. guardar el contacto en "estado.txt"
        conductor=libreria.pedir_nombre("ingrese el nombre del conductor:")
        estado=libreria.pedir_estado("ingrese el estado del conductor(ebrio-sano): ")
        contenido=conductor+" - "+estado+"\n"
        libreria.agregar_datos("estado.txt",contenido,"a")
        print("los datos del conductor se guardaron con exito")
    def opcionB():
        #4. acceder al archivo estado.txt y mostrar los datos
        datos=libreria.obtener_datos("estado.txt")
        print("conductor - estado")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("#### DATOS DEL CONDUCTOR #####")
        print("#1. agregar datos del conducto")
        print("#2. mostrar datos del conductor")
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
    print("#1. Agregar datos del auto ")
    print("#2. Agregar datos del conductor")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
