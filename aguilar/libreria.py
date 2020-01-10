def validar_entero(num):
    if(isinstance(num,int)):
        if(num>0):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_num(msg):
    n=0
    while(validar_entero(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return n
#fin_def

def validar_rango(num,ri,rf):
    if(validar_entero(num)==True):
        if(num>=ri and num<=rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_numero(msg,ri,rf):
    n=0
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return int(n)
#fin_def

# Devuelve true si es un nombre
# O False si no es lo que pide
def  validar_nombre(nombre):
    #verificamos si es un numero
    if(isinstance(nombre, str)):
        #ahora verificamos si tiene mas de 3 caracteres
        if(len(nombre)>=3):
            if(nombre.isdigit()==False):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    #fin_if
#fin_def

def pedir_nombre(msg):
    nom=""
    while(validar_nombre(nom)==False):
        nom=input(msg)
    return nom
#fin_def

def validar_tamano(tam):
    if(isinstance(tam,str)):
        tam=tam.lower()
        if(tam=="pequeño" or tam=="mediano" or tam=="grande"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_tamano(msg):
    t=""
    while(validar_tamano(t)==False):
        t=input(msg)
    return t
#fin_def

# Devuelve true si es un real
# O False si no es lo que pide
def  validar_real(real):
    #verificamos si es un real
    if(isinstance(real, float)):
        if(real>0.0):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_def

def pedir_real(msg):
    re=0.0
    while(validar_real(re)==False):
        re=input(msg)
        if(re.isdigit()==False):
            re=float(re)
    return re
#fin_def

def validar_tipo(tipo):
    if(isinstance(tipo,str)):
        tipo=tipo.lower()
        if(tipo=="nombrado" or tipo=="empleado" or tipo=="contratado"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_tipo(msg):
    ti=""
    while(validar_tipo(ti)==False):
        ti=input(msg)
    return ti
#fin_def

def validar_ruc(ruc):
    if(isinstance(ruc,int)):
        if(ruc>0):
            if(len(str(ruc))==11):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_ruc(msg):
    ruc=0
    while(validar_ruc(ruc)==False):
        ruc=input(msg)
        if(ruc.isdigit()==True):
            ruc=int(ruc)
    return int(ruc)
#fin_def

def validar_juego(juego):
    if(isinstance(juego,str)):
        if(juego=="mario" or juego=="pes"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_juego(msg):
    ju=""
    while(validar_juego(ju)==False):
        ju=input(msg)
    return ju
#fin_def

def validar_dni(dni):
    if(isinstance(dni,int)):
        if(dni>0):
            if(len(str(dni))==8):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_dni(msg):
    dni=0
    while(validar_dni(dni)==False):
        dni=input(msg)
        if(dni.isdigit()==True):
            dni=int(dni)
    return dni
#fin_def

def validar_ciclo(ciclo):
    if(isinstance(ciclo,str)):
        ciclo=ciclo.lower()
        if(ciclo=="primero" or
            ciclo=="segundo" or
            ciclo=="tercero" or
            ciclo=="cuarto" or
            ciclo=="quinto" or
            ciclo=="sexto" or
            ciclo=="septimo" or
            ciclo=="octavo" or
            ciclo=="noveno" or
            ciclo=="decimo"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_ciclo(msg):
    ciclo=""
    while(validar_ciclo(ciclo)==False):
        ciclo=input(msg)
    return ciclo
#fin_def

def validar_tar(tar):
    if(isinstance(tar,str)):
        #1.el numero de tar tiene 3 espacios
        data=tar.split(" ")
        if(len(data)!=4):
            return False
        #2. igualamos variables
        oct1=str(data[0])
        oct2=str(data[1])
        oct3=str(data[2])
        oct4=str(data[3])
        if(oct1.isdigit()==False or oct2.isdigit()==False or oct3.isdigit()==False or oct4.isdigit()==False):
            return False

        #3.LOS RANGOS
        oct1=int(data[0])
        oct2=int(data[1])
        oct3=int(data[2])
        oct4=int(data[3])
        if(validar_rango(oct1,0,9999)==True or
            validar_rango(oct2,0,9999)==True or
            validar_rango(oct3,0,9999)==True or
            validar_rango(oct4,0,9999)==True):
            if(len(str(oct1))==4 and len(str(oct2))==4 and
                len(str(oct3))==4 and len(str(oct4))==4):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_tar(msg):
    tar=""
    while(validar_tar(tar)==False):
        tar=input(msg)
    return tar
#fin_def

def validar_clave(clave):
    if(isinstance(clave,int)):
        if(len(str(clave))==4):
            if(clave>=0 and clave<=9999):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_clave(msg):
    cla=0
    while(validar_clave(cla)==False):
        cla=input(msg)
        if(cla.isdigit()==True):
            cla=int(cla)
    return cla
#fin_def

def validar_tel(tel):
    if(isinstance(tel,str)):
        #1.el numero telefonico tiene un espacio
        data=tel.split(" ")
        if(len(data)!=2):
            return False
        #2.igualamos
        num1=str(data[0])
        num2=str(data[1])
        if(num1.isdigit()==False or num2.isdigit()==False):
            return False
        #3.validamos los verdareros digitos
        num1=tel[0:3]
        num2=tel[4:]
        if(str(num1)!="074"):
            return False
        if(len(num2)==6):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_telefono(msg):
    tel=""
    while(validar_tel(tel)==False):
        tel=input(msg)
    return tel
#fin_def

def validar_celular(cel):
    if(isinstance(cel,int)):
        if(len(str(cel))==9):
            if(int(str(cel)[0])==9):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_celular(msg):
    cel=0
    while(validar_celular(cel)==False):
        cel=input(msg)
        if(cel.isdigit()==True):
            cel=int(cel)
    return int(cel)
#fin_def

def validar_mess(mes):
    if(isinstance(mes,str)):
        mes=mes.lower()
        if(mes=="diciembre" or mes=="enero" or
            mes=="febrero" or mes=="marzo" or
            mes=="abril" or mes=="mayo" or
            mes=="junio" or mes=="julio" or
            mes=="agosto" or mes=="septiembre" or
            mes=="octubre" or mes=="noviembre"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_mes(msg):
    mes=""
    while(validar_mess(mes)==False):
        mes=input(msg)
    return  mes
#fin_def

def validar_correo(correo):
    #verificamos si el correo es correcto
    if(isinstance(correo,str)):
        cor=correo[::-1]
        if(cor[0:10]=="moc.liamg@"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_correo(msg):
    cor=""
    while(validar_correo(cor)==False):
        cor=input(msg)
    return cor
#fin_def

def validar_hotmail(hot):
    #verificamos si el correo es correcto
    if(isinstance(hot,str)):
        cor=hot[::-1]
        if(cor[0:12]=="moc.liamtoh@"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_hot(msg):
    hot=""
    while(validar_hotmail(hot)==False):
        hot=input(msg)
    return hot
#fin_def

def validar_placa(pla):
    if(isinstance(pla,str)):
        data=pla.split("-")
        if(len(data)!=2):
            return False
        cad=data[0]
        num=str(data[1])
        if(cad!=cad.upper()):
            return False
        if(cad[1].isdigit()==False):
            return False
        if(num.isdigit()==False or cad.isdigit()==True):
            return False
        if(len(num)!=3 or len(cad)!=3):
            return False
        else:
            return True
    else:
        return False
#fin_def

def pedir_placa(msg):
    pla=""
    while(validar_placa(pla)==False):
        pla=input(msg)
    return pla
#fin_def

def validar_color(color):
    if(isinstance(color,str)):
        color=color.lower()
        if(color=="negro" or color=="blanco" or
            color=="azul" or color=="amarillo" or
            color=="verde" or color=="naranja" or
            color=="plomo" or color=="marron" or
            color=="rojo" or color=="celeste"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_color(msg):
    color=""
    while(validar_color(color)==False):
        color=input(msg)
    return  color
#fin_def

def validar_estado(estado):
    if(isinstance(estado,str)):
        estado=estado.lower()
        if(estado=="sano" or estado=="ebrio"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_estado(msg):
    est=""
    while(validar_estado(est)==False):
        est=input(msg)
    return est
#fin_def

def validar_codigo(cod):
    if(isinstance(cod, str)):
        if(len(cod)!=7):
            return False
        num=cod[0:6]
        if(num.isdigit()==False):
            return False
        cad=cod[6]
        if(cad.isdigit()==True):
            return False
        else:
            return True
    else:
        return False
#fin_def

def pedir_codigo(msg):
    cod=""
    while(validar_codigo(cod)==False):
        cod=input(msg)
    return cod
#fin_def

def validar_tipo_de_pago(pago):
    if(isinstance(pago, str)):
        pago=pago.lower()
        if(pago=="efectivo" or pago=="tarjeta"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_tipo_de_pago(msg):
    tipo=""
    while(validar_tipo_de_pago(tipo)==False):
        tipo=input(msg)
    return tipo
#fin_def

def validar_rang(num,ri,rf):
    if(validar_real(num)==True):
        if(num>=ri and num<=rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_nota(msg,ri,rf):
    re=0.0
    while(validar_rang(re,ri,rf)==False):
        re=input(msg)
        if(re.isdigit()==False):
            re=float(re)
    return re
#fin_def

# Devuelve true si año es un año valido
def validar_año(año):
    # Verificar si año es una cadena
    # Verificar si año tiene 4 caracteres
    # Verificar si año tiene forma de numeros
    # Verificar si el año esta entre 0 y 9999
    if ( isinstance(año, str) ):
        if ( len(año) == 4 ):
            if ( año.isdigit() == True ):
                if ( int(año) > 0 and int(año) <= 9999 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def validar_mes(mes):
    # Verificar si mes es una cadena
    # Verificar si mes tiene 2 caracteres
    # Verificar si mes tiene forma de numeros
    # Verificar si el mes esta entre 0 y 12
    if ( isinstance(mes, str) ):
        if ( len(mes) == 2 ):
            if ( mes.isdigit() == True ):
                if ( int(mes) > 0 and int(mes) <= 12 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def validar_dia(dia):
    # Verificar si dia es una cadena
    # Verificar si dia tiene 2 caracteres
    # Verificar si dia tiene forma de numeros
    # Verificar si el dia > 0 y <= 31
    if ( isinstance(dia, str) ):
        if ( len(dia) == 2 ):
            if ( dia.isdigit() == True ):
                if ( int(dia) > 0 and int(dia) <= 31 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def validar_fecha(fecha):
    # LA fecha es una cadena
    # La fecha tienen 10 caracteres
    # YYYY-MM-DD (hay 2 caracteres -)
    # YYYY es un año valido
    # MM es un mes valido
    # DD es un dia valido
    if ( isinstance(fecha, str) ):
        if ( len(fecha) == 10 ):
            if( fecha[4] == "-" and fecha[7] == "-" ):
                año=fecha[0:4]
                mes=fecha[5:7]
                dia=fecha[8:]
                if ( validar_año(año) == True
                    and validar_mes(mes) == True
                    and validar_dia(dia) == True):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_fecha(msg):
    fe=""
    while(validar_fecha(fe)==False):
        fe=input(msg)
    return fe
#fin_def

def agregar_datos(file,contenido,modo):
    archivo=open(file,modo)
    archivo.write(contenido)
    archivo.close()
#fin_def

def obtener_datos(ruta_archivo):
    archivo=open(ruta_archivo,"r")
    datos=archivo.read()
    archivo.close()
    return datos
#fin_def

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista
#fin_def

def mostrar_separacion(rut_archivo):
    archivo=open(rut_archivo)
    datos=archivo.readlines()
    lista_1=[]
    lista_2=[]
    for item in datos:
        p1,p2=item.split("-")
        lista_1.append(p1.replace("\n",""))
        lista_2.append(p2.replace("\n",""))
    archivo.close()
    return lista_1,lista_2
#fin_def

def mostrar_separacion2(rut_archivo):
    archivo=open(rut_archivo)
    datos=archivo.readlines()
    lista_1=[]
    lista_2=[]
    lista_3=[]
    for item in datos:
        p1,p2,p3=item.split("-")
        lista_1.append(p1.replace("\n",""))
        lista_2.append(p2.replace("\n",""))
        lista_3.append(p3.replace("\n",""))
    archivo.close()
    return str(lista_1)+ "\n"+str(lista_2)+"\n"+str(lista_3)
#fin_def

def sumar(pes1,pes2):
    sum=(float(pes1)-float(pes2))
    return sum
#fin_def

def promedio(nota1,nota2,nota3):
    prom=(float(nota1)+float(nota2)+float(nota3))/3
    return prom
#fin_def
