#ESTA FUNCION NOS PERMITE VALIDAD SI UN NUMERO EN ENTERO POSITIVO
#sI EL NUMERO INTRODUCIDO ES NEGATIVO RETORNA FALSE
def validar_entero_positivo(num):
    # 1. La instancia de num es int
    # 2. num > 0
    if (isinstance(num,int)):
        if (num > 0):
            return True
        else:
            return False
    else:
        return False
# fin_def

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS PERMITE VALIDAD UNA NOTA
#CONSISTE QUE EL NUMERO DE LA NOTA SE ENCUENTRA ENTRE EL RANGO 1 Y 20,
def validar_nota(num):
    # 1. La instancia de num es int
    # 2. num > 0
    if (isinstance(num,int)):
        if (num > 0 and num<=20):
            #sI EL NUMERO INTROSUCIDO ES MAYOY QUE CERO Y MENOR A 20 RETORNA TRUE
            return True
        else:
            return False
    else:
        return False

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS PERMITE PEDIR UNA NOTA QUE SE ENCUENTRA EN EL TRANGO DE 0 Y 20
#SI SE INGRESA UN NUMERO INCORRECTO, VULEVE A PEDIR

def pedir_nota(msg):
    n=0
    while(validar_nota(n)==False):
        n=input(msg)
        if (n.isdigit()):
            n=int(n)
    #fin while
    return int(n)

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS VALIDA EL NUMERO DE UN DNI
#SI SE INGRESA MENOS DE 8 DIGITOS O MAS DE 8 DIGITOS,RETORNA FALSE
def validar_dni(dni):
    if (isinstance(dni,int) and len(str(dni))==8):
        return True
    else:
        return False

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA OPCION JUNTO CON LA OPCION VALIDAD DNI, NOS PERMITE PEDIR QUE SE INGRESE EL DNI
#SI SE INGRESARA DATOS INCORRECTOS VUELVE A PEDIR DNI
def pedir_dni(msg):
    n="ssw"
    while(validar_dni(n)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    # fin_while
    return int(n)

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS VALIDA EL NUMERO TELEFONICO, EL CUAL TIENE UNA LONGITUD DE 9 DIGITOS
#SISE INGRESARA UNA LOGITUD DIEFENTE DE 9 , RETORNA FALSE

def validar_telefono(telf):
    if (isinstance(telf,int) and len(str(telf))==9):
        return True
    else:
        return False

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS PEDIRA , QUE INCERTEMOS  UN NUMERO DE LONGITUD 9
#SI LA LONGITUD ES DIFERENTE DE 9 ,  VUELVE A PEDIR
def pedir_telefono(msg):
    n="ssw"
    while(validar_telefono(n)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    # fin_while
    return int(n)

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION MAS COMPLETA, NOS VALIDA UN NUMERO, Y NOS PERMITE PONER EL RANGO QUE CREAMOS CONVENIENTE
#ESTA FUNCION VA DE LA MANO CON LA FUNCION VALIDAR_ENTERO_POSITIVO

def validar_rango(num,ri,rf):
    # 1. Es un entero positivo
    # 2. Esta dentro del rango
    if (validar_entero_positivo(num) == True):
        if (num >= ri and num <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_def
#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION NOS PERMITE PEDIR UN MENSAJE, Y EL RANGO QUE DESEEMOS
#ESTA FUNION NOS PIDE UN NUMERO, Y EL RANGO INTRODUCIDO DEBE ESTAR TAL NUMERO
def pedir_entero(msg,ri,rf):
    n=0
    while(validar_entero_positivo(n)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    # fin_while
    return int(n)
#fin_def
#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION ES ALGO SIMILIAR A UNA FUNCION ANTEORIO, ESTA FUNCION RETONE EL DIGITO INTRODUCIDO
#SOLO SIRVE PARA INTRODUCIR VALORES POSITIVOS
def pedir_entero_positivo(num):
    n=0
    while(validar_entero_positivo(n)==False):
        n=input(num)
        if (n.isdigit()):
            n=int(n)
    #fin while
    return int(n)

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION, NOS PERMITE VALIRDA UN NOMBRE, EL CUAL DEBE SER MAYOR QUE TRES DIGITOS
#SI LA CADENA INTRODUCIDA ES MENOR A TRES DIGITOS RETORNA FALSE
def validar_nombre(nombre):
    if (isinstance(nombre,str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION ME PIDE INTRODUCIR UNA CADENA ASYOR A TRES DIGITOS
#SI LA CADENA ES CORRECTA RETORNA LA CADEA
def pedir_nombre(msg):
    nombre=""
    while (validar_nombre(nombre) == False):
        nombre= input(msg)
    #fin while
    return nombre
#fin pedir nombre

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION ES MUY IMPORTANTE, PORQUE ME PERMITE AGREGAR DATOS A UN ARCHIVO EXTERIR
#PODEMOS AGREGAR CUALQUIER TIPO DE DATO
def agregar_datos(ruta_archivo,contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION VA DE LA MANO CON LA ANTERIOR FUNCION PUES QUE LA ANTERIOR SU FUNCION ES AGREGAR DATOS
#ESTA FUNCION NOS PERMITE MOSTRAR LOS DATOS AGREGADOS ANTERIROMENTE, LOS PODEMOS HACER CON DIFERENTES OPCIONES

def obtener_datos(ruta_archivo):
    archivo=open(ruta_archivo,"r")
    datos=archivo.read()
    archivo.close()
    return datos

#*************************************************************************************************************
#*************************************************************************************************************


#ESTA FUNCION ES MUY INTERESANTE PUESTO QUE ME PERMITE ORDENAR LISTA DATOS VALIDADOS
#ME PERMITE LEER EL ARCHIVO LINEA POR LINEA
def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION ME PERMITE VAIDA UN IP, EL CUAL SU ESTRUCTURA ES 255.255.255.255 DESDE CERO HASTA 255
#CADA NUMERO ESTA SEPARADO POR PUNTOSS
def validar_ip(ip):
    # 1. Revisar que el nro de octetos sea 4
    data=ip.split(".")
    if ( len(data) != 4):
        return False

    # 2. Los 4 octetos deben ser enteros
    oct1 = data[0]
    oct2 = data[1]
    oct3 = data[2]
    oct4 = data[3]
    if ( oct1.isdigit() == False or oct2.isdigit() == False or
         oct3.isdigit() == False or oct4.isdigit() == False):
        return False

    # 3. Cada octeto esta entre 0 y 255
    oct1 = int(data[0])
    oct2 = int(data[1])
    oct3 = int(data[2])
    oct4 = int(data[3])
    if ( validar_rango(oct1, 0, 255) == False or
         validar_rango(oct2, 0, 255) == False or
         validar_rango(oct3, 0, 255) == False or
         validar_rango(oct4, 0, 255) == False):
        return False

    # 4. Si llego hasta aqui, es porque es un IP valido
    return True
#fin_validar

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION VA DE LA MANO CON LA ANTERIOR FUNCION , LO DIEFERNTE ES QUE ESTA FUNCION TE PIDE INTRODUCIR EL IP
#SI EL IP INTRODUCIDO ES INCORRECTO, TE PIDE INTROSUCIR DE NUEVO EL IP
def pedir_ip(msg):
    ip_invalido=True
    while( ip_invalido == True ):
        ip=input(msg)
        ip_invalido = ( validar_ip(ip) == False)
    #fin_while
    return ip

#*************************************************************************************************************
#*************************************************************************************************************

#ESTA FUNCION CONSISTE EN PEDIR UN NUMERO , QUE SE ENCUENTRA EN RANGO, NOSOTROS MISMO INTRODUCIMOS EL RANGO
#SI LOS DIGITOS INTRODUCIDOS SON LETRAS ME VUELVE A PEDIR LOS DIGITOS
def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero
#*************************************************************************************************************
#*************************************************************************************************************
