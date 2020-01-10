import libreria
def opcion1():
    def opcionA():
        #1. pedir el nombre de usuario
        #2. pedir el correo de gmail
        #3. guardar los datos en "gmail.txt"
        nombre=libreria.pedir_nombre("ingrese el nombre de usuario:")
        correo=libreria.pedir_correo("ingrese su correo electronico (******@gmail.com): ")
        contenido=nombre+" - ("+correo+")\n"
        libreria.agregar_datos("gmail.txt",contenido,"a")
        print("los datos de su correo han sido guardado con exito")
    def opcionB():
        #4. acceder al archivo gmail.txt y mostrar los datos
        datos=libreria.obtener_datos("gmail.txt")
        print("usuario - correo")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("############ GMAIL ###########")
        print("#1. agregar correo de gmail")
        print("#2. mostrar los correos guardados")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el nombre de usuario
        #2. pedir el correo de hotmail
        #3. guardar los datos "hotmail.txt"
        usuario=libreria.pedir_ruc("ingrese su nombre de usuario:")
        correo=libreria.pedir_nombre("ingrese su correo electronico(******@hotmail.com): ")
        contenido=usuario+"-("+correo+")\n"
        libreria.agregar_datos("hotmail.txt",contenido,"a")
        print("su correo de hotmail ha sido guardado con exito")
    def opcionB():
        #4. acceder al archivo hotmail.txt y mostrar los datos
        datos=libreria.obtener_datos("hotmail.txt")
        print("usuario - correo")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("########## HOTMAIL ###########")
        print("#1. Agragar correo de hotmail")
        print("#2. Mostrar correos guardados")
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
    print("########## CUENTAS ############")
    print("#1. Por gmail ")
    print("#2. Por hotmail")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
