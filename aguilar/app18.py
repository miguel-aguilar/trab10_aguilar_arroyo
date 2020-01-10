import libreria
def opcion1():
    def opcionA():
        #1. pedir el producto que desea llevar
        #2. pedir el total que va a llevar
        #3. guardar los datos en "producto.txt"
        producto=libreria.pedir_nombre("ingrese el producto que desea llevar:")
        unidades=libreria.pedir_num("ingrese las unidades que desea llevar: ")
        contenido=producto+" - "+str(unidades)+"\n"
        libreria.agregar_datos("producto.txt",contenido,"a")
        print("los datos de la compra han sido guardados")
    def opcionB():
        #4. acceder al archivo producto.txt y mostrar los datos
        print("producto - unidades")
        datos=libreria.obtener_datos("producto.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### PRODUCTO #######")
        print("#1. AGREGAR EL PRODUCTO QUE DESEA LLEVAR")
        print("#2. MOSTRAR LOS PRODUCTO QUE VA A LLEVAR")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el tipo de pago
        #2. pedir el nombre del cliente
        #3. guardar el contacto en "tipo_de_pago.txt"
        tipo=libreria.pedir_tipo_de_pago("ingrese el tipo de pago(efectivo/tarjeta) :")
        cleinte=libreria.pedir_nombre("ingrese el nombre del cliente: ")
        contenido=cleinte+" - "+tipo+"\n"
        libreria.agregar_datos("tipo_de_pago.txt",contenido,"a")
        print("los datos del tipo de pago se guardaron con exito")
    def opcionB():
        #4. acceder al archivo tipo_de_pago.txt y mostrar los datos
        datos=libreria.obtener_datos("tipo_de_pago.txt")
        print("cleinte - tipo de pago")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("######## TIPO DE PAGO #########")
        print("#1. Agregar la forma en que se va a pagar")
        print("#2. Mostrar la forma en que se va a pagar")
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
    print("########## MAYORISTA #############")
    print("#1. Agregar producto ")
    print("#2. Agregar el tipo de pago")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
