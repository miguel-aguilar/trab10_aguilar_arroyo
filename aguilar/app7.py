import libreria
def opcion1():
    #1. pedir el nombre del curso
    #2. pedir el numero de creditos (1-7)
    #3. guardar datos en "cursos.txt"
    curso=libreria.pedir_nombre("ingrese el nombre del curso: ")
    peso=libreria.pedir_numero("ingrese el numero de creditos del curso que acaba de agregar: ",1,7)
    contenido=curso+"-"+str(peso)+"\n"
    libreria.agregar_datos("cursos.txt",contenido,"a")
    print("su curso a sido guardado con exito")
def opcion2():
    #4. acceder al archivo cursos.txt y mostrar los datos
    datos=libreria.obtener_datos("cursos.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
    #5. acceder archivo curso.txt y separar los nombres de los cursos con el numero de creditos
def opcion3():
    sep=libreria.mostrar_separacion("cursos.txt")
    print(sep)
opc=0
max=4
while(opc!=max):
    print("########## inscripcion ################")
    print("# 1. Agregar cursos ")
    print("# 2. Mostrar cursos agregados ")
    print("# 3. Mostrar cursos y el numero de creditos por separado")
    print("# 4. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,4)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
    if(opc==3):
        opcion3()
print("fin del programa")
