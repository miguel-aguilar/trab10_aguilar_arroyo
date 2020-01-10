import libreria
def opcion1():
    def opcionA():
        #1. pedir el codigo del estudiante
        #2. guardar los datos en "reporte.txt"
        codigo=libreria.pedir_codigo("ingrese el codigo del estudiante:")
        contenido=codigo+"\n"
        libreria.agregar_datos("reporte.txt",contenido,"a")
        print("el codigo se ha guardado con exito")
    def opcionB():
        #3. acceder al archivo reporte.txt y mostrar los datos
        print("##### REPORTES #####")
        print("CODIGO:")
        datos=libreria.obtener_datos("reporte.txt")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### CODIGO #######")
        print("#1. AGREGAR CODIGO")
        print("#2. MOSTRAR LOS CODIGOS GUARDADOS")
        print("#3. salir")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion: ",1,3)
        if(opc==1):
            opcionA()
        if(opc==2):
            opcionB()
def opcion2():
    def opcionA():
        #1. pedir el nombre del alumno
        #2. pedir el ciclo en que esta el estudiante
        #3. guardar los datos en "estudiante.txt"
        estudiante=libreria.pedir_nombre("ingrese el nombre del estudiante reportado:")
        ciclo=libreria.pedir_ciclo("ingrese el ciclo en que se encuentra(primero,segundo,tercero,cuarto,quinto,"
                                     "sexto,septimo,octavo,noveno,decimo): ")
        contenido=estudiante+" - "+ciclo+"\n"
        libreria.agregar_datos("estudiante.txt",contenido,"a")
        print("los datos del estudiante se guardaron con exito")
    def opcionB():
        #4. acceder al archivo estudiante.txt y mostrar los datos
        datos=libreria.obtener_datos("estudiante.txt")
        print("##### REPORTES #####")
        print("ESTUDIANTE - CICLO")
        if(datos!=""):
            print(datos)
        else:
            print("archivo vacio")
    opc=0
    max=3
    while(opc!=max):
        print("###### ESTUDIANTE-CICLO ######")
        print("#1. Agregar datos del esudiente")
        print("#2. Mostrar datos del estudiante")
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
    print("########## REPORTE #############")
    print("#1. Por codigo ")
    print("#2. Por nombre y ciclo")
    print("#3. Salir")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
