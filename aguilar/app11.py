import libreria
def opcionTelefono():
    def opcionA():
        #1. pedir el numero TELEFONICO
        #2. pedir el nombre del nuevo contacto
        #3. guardar el contacto en "agenda_tel.txt"
        telefono=libreria.pedir_telefono("ingrese su numero de telefono (074 ******):")
        nombre=libreria.pedir_nombre("ingrese el nombre del contacto: ")
        contenido=nombre+"-("+str(telefono)+")\n"
        libreria.agregar_datos("agenda_tel.txt",contenido,"a")
        print("su contacto ha sido guardado con exito")
    def opcionB():
        #4. acceder al archivo agenda_tel.txt y mostrar los datos
        datos=libreria.obtener_datos("agenda_tel.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("########### TELEFONO #########")
        print("#1. agregar numero telefonico")
        print("#2. mostrar contacto")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcionCelular():
    def opcionA():
        #1. pedir el numero de calular
        #2. pedir el nombre del nuevo contacto
        #3. guardar el contacto en "agenda_cel.txt"
        celular=libreria.pedir_celular("ingrese su numero de celular (9********):")
        nombre=libreria.pedir_nombre("ingrese el nombre del contacto: ")
        contenido=nombre+"-("+str(celular)+")\n"
        libreria.agregar_datos("agenda_cel.txt",contenido,"a")
        print("su contacto ha sido guardado con exito")
    def opcionB():
        #4. acceder al archivo agenda_cel.txt y mostrar los datos
        datos=libreria.obtener_datos("agenda_cel.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("########### CELULAR #########")
        print("#1. agregar numero ce calular")
        print("#2. mostrar contacto")
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
    print("########## AGENDA #############")
    print("#1. Numero telefonico ")
    print("#2. Numero de celular")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcionTelefono()
    if(opc==2):
        opcionCelular()
print("fin del programa")
