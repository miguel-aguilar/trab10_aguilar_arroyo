import libreria
def opcion1():
    def opcionA():
        #1. pedir el las notas de los siguientes criterios:
        #2. guardar los datos en "matematica_basica.txt"
        nota1=libreria.pedir_nota("ingrese la nota de su primer examen:",0.0,20.0)
        nota2=libreria.pedir_nota("ingrese la nota de su segundo examen: ",0.0,20.0)
        nota3=libreria.pedir_nota("ingrese la nota de su examen final: ",0.0,20.0)
        contenido=str(nota1)+"-"+str(nota2)+"-"+str(nota3)+"\n"
        libreria.agregar_datos("matematica_basica.txt",contenido,"a")
        print("tus notas se han guardado exitosamente")
    def opcionB():
        #3. acceder al archivo MATEMATICA_BASICA.txt y ver la variacion de tu peso
        print("(nota1) - (nota2) - (nota3) - (promedio)")
        datos=libreria.obtener_datos_lista("matematica_basica.txt")
        for linea in datos:
            linea = linea.replace("\n", "")
            nota1, nota2 ,nota3= linea.split("-")
            promedio=libreria.promedio(nota1,nota2,nota3)
            print("("+str(nota1) + ") - (" + str(nota2) + ") - (" + str(nota3)+") - ("+str(promedio) + ")")
    opc=0
    max=3
    while(opc!=max):
        print("##### MATEMATICA BASICA I #####")
        print("#1. AGREGAR NOTAS ")
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
        #1. pedir el las notas de los siguientes criterios:
        #2. guardar los datos en "programacion.txt"
        nota1=libreria.pedir_nota("ingrese la nota de su primer examen:",0.0,20.0)
        nota2=libreria.pedir_nota("ingrese la nota de su segundo examen: ",0.0,20.0)
        nota3=libreria.pedir_nota("ingrese la nota de su examen final: ",0.0,20.0)
        contenido=str(nota1)+"-"+str(nota2)+"-"+str(nota3)+"\n"
        libreria.agregar_datos("programacion.txt",contenido,"a")
        print("tus notas se han guardado exitosamente")
    def opcionB():
        #3. acceder al archivo programacion.txt y ver la variacion de tu peso
        print("(nota1) - (nota2) - (nota3) - (promedio)")
        datos=libreria.obtener_datos_lista("programacion.txt")
        for linea in datos:
            linea = linea.replace("\n", "")
            nota1, nota2 ,nota3= linea.split("-")
            promedio=libreria.promedio(nota1,nota2,nota3)
            print("("+str(nota1) + ") - (" + str(nota2) + ") - (" + str(nota3)+") - ("+str(promedio) + ")")
    opc=0
    max=3
    while(opc!=max):
        print("######## PROGRAMACION I ########")
        print("#1. AGREGAR NOTAS ")
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
    print("########## CURSOS #############")
    print("#1. MATEMATICA BASICA I")
    print("#2. PROGRAMACION I")
    print("#3. SALIR")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
