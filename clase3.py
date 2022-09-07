# e = ["NOMBRE", "EST DAT", "PROG FUNC", "INGLES"]
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
# m_e_d= (9,8,7,6)
# m_e_p= (9,5,9,8)
# m_e_f= (9,8,7,6)
# m_e_ñ= (9,8,7,6)

# ##MANDAR EL REPORTE A UNA FUNCION 

# def reporte (msj=int): 
#     print (f"{e[0]:^{msj}}{e[1]:^{msj}}{e[2]:^{msj}}{e[3]:^{msj}}")
#     for i in range (len(alumnos)): 
#         print (f"{alumnos [i]:*^{msj}}{m_e_d[i]:*^{msj}} {m_e_p[i]:*^{msj}} {m_e_f[i]:*^{msj}} {m_e_ñ[i]:*^{msj}}")

# if __name__=="__main__": 
#     reporte(25)

# numeroBig = 124668952487529  ##SEPARACION CON COMAS
# print(f"{numeroBig: ,d}")
# ##
# numeroPI = 3.14164578953216458 ##LO IMRIME DEJANDO ESPECIFICAMENTE SOLAMENTE LOS ULTIMOS 3 DECIMALES DE LA CANTIDAD 
# print(f"{numeroPI: .3f}")

# ##NOTACION CIENTIFICA 
# numeroPI2 = 314.45896513258
# print(f"{numeroPI2: .2e}")

# ##PORCENTAJE 
# numeroporcentaje = 0.25689412654
# print(f"{numeroporcentaje:%}")
# print (f"{numeroporcentaje:.2%}") ##TE CONVIERTE DE NUMERO DECIMAL A PORCENTAJE Y TE DEJA LOS ULTIMOS DOS DIGITOS DEL DECIMAL

# #NUMEROS BINARIOS 
# print(f"{25:b}")

# #UNICODES 
# print (f"{13:c}")

# #HEXADECIMAL 
# print (f"{255:x}")

# ##OCTAL 
# print(f"{255: o}")


##ESCRIBA UNA FUNCION QUE GENERE UNA TABLA DE MULTIPLICAR 
##RECIBIENDO COMO ARGUMENTO LA CANTIDAD DE NUM A GENERAR

# def tabla_multi(n= int, n2=int):  ##PRODUCTO 

#     for i in range (1, n+1):
#      print(i*n2)

def producto (a= int, b= int)-> int: return a*b

def tablas(m= int, n= int, fmt= int) -> int: 
    for i in range (1, n+1):
        tablas(n, i, fmt)

def tablas_mult(n:int, n2= int, fmt= int): ##SE CREA UN CONTADOR PARA PODER CREAR UN CICLO, RANGO ES EL 
    for i in range (1, n+1):
        print(f"{n2:^{fmt}}x{i:^{fmt}} = {producto(a= int, b=int):^{fmt}}")
    print()

if __name__=="__main__": 
    tablas_mult(3,4,6)


