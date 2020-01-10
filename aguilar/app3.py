import libreria
def opcion1():
    #1. pedir el nombre del alumno
    #2. pedir la ficha de notas
    #3. guardar datos en "notas.txt"
    alumno=libreria.pedir_nombre("ingrese el nombre del alumno: ")
    notas=libreria.pedir_nota("ingrese la nota: ",0.0,20.0)
    contenido=alumno+" obtuvo la nota de: "+str(notas)+"\n"
    libreria.agregar_datos("notas.txt",contenido,"a")
    print("su nota se guardo con exito")
def opcion2():
    #1. acceder al archivo notas.txt y mostrar los datos
    datos=libreria.obtener_datos("notas.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo vacio")
opc=0
max=3
while(opc!=max):
    print("########## NOTAS ################")
    print("# 1. añadir NOTA ")
    print("# 2. mostrar NOTAS ")
    print("# 3. salir ")
    print("#######################################")
    opc=libreria.pedir_numero("ingrese opcion: ",1,3)
    if(opc==1):
        opcion1()
    if(opc==2):
        opcion2()
print("fin del programa")
