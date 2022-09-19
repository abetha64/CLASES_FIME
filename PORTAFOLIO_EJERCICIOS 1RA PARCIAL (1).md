# UNIVERSIDAD DE COLIMA 
![https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png]
 ### FACULTAD DE INGENIERÍA MECÁNICA Y ELÉCTRICA
 ###  Ingeniería en Computación Inteligente
### Programación Funcional 
### Alumno: Alba Beth-birai López Aguilar 20186885
### Profesor: Dr. Walter Alexander Mata 
##                                                                                                    

 <div style= "text-align: justify"> Objetivos: Programación funcional en Python. </div>
 <div style= "text-align: justify"> Desarrollo: </div>
   <div style= "text-align: justify"> Durante la parcial se impartió temas derivados de la programacion dinámica, se vió como tal, funciones, listas, sets, diccionarios (ejemplos) y las fstrings dentro del lenguaje, a continuación se presentan los ejercicios y ejemplos en clase </div>

### CLASE 1. FUNCIONES.  
### OPERACIONES BÁSICAS. 
<div style= "text-align: justify">  Funciones de operaciones básicas, se muestran a continuación una función por cada tipo de operación: suma, multiplicacion y división </div>


```python
def sumar(a: int, b: int)-> int:
    return a+b

if __name__ == "__main__": 
    print (sumar(5,6))
    
def restar(a: int, b: int)-> int:
return a-b

if __name__ == "__main__": 
    print (restar(10,6))
    
def  dividir(a: float, b: float)-> float:
    return a/b

if __name__ == "__main__": 
    print (dividir(12,6))
    
def  multiplicar(a: float, b: float)-> float:
return a*b

if __name__ == "__main__": 
    print (multiplicar(5,6))

def  cuadrado(a: int)-> int:
return a*a

if __name__ == "__main__": 
    print (cuadrado(5))
```

## Clase2. 
## TEMA-.> Importación de funciones y ser llamadas externamente.  
Se importa y crea una librería para poder crar un modulo, la facilidad de esto es poder utilizar la libreria en varios dispositivos. 
En el archivo operaciones se encuentra las funciones de suma y resta hasta el cuadrado, éstas son llamadas para con la palabra reservada "import" y el nombre de la función, en este ejemplo se muestra el "as" el cual es un alias para poder "llamarla" de manera directa a la hora de ser impresa. Cabe recalcar que para ser llamadas las funciones es necesario que ambos archivos estén dentro de la misma carpeta para que no haya problema alguno. 


```python
##CARPETA OPERACIONES: 
def sumar(a: int, b: int)-> int:
    return a+b

def restar(a: int, b: int)-> int:
    return a-b

def  multiplicar(a: float, b: float)-> float:
    return a*b

def  dividir(a: float, b: float)-> float:
    return a/b

def  cuadrado(a: int)-> int:
    return a*a

 ##FORMA DE IMPORTACIÓN 1 
    import sumar as s 
    import restar as a
    import multiplicar as b
    import dividir as c
    import cuadrado as d
 
    if __name__ == "__main__": 
        print (s.sumar(5,6))
        print (a.restar(10,6))
        print (b.multiplicar(5,6))
        print (c.dividir (12,6))
        print (d.cuadrado (5))

        

```

DIFERENTES FORMAS DE IMPORTACIONES DE ARCHIVOS: 



```python
##CARPETA OPERACIONES: 
def sumar(a: int, b: int)-> int:
    return a+b

def restar(a: int, b: int)-> int:
    return a-b

def  multiplicar(a: float, b: float)-> float:
    return a*b

def  dividir(a: float, b: float)-> float:
    return a/b

def  cuadrado(a: int)-> int:
    return a*a

from operaciones import *

    if __name__ == "__main__":
        print(sumar (5,6))
        print (restar(10,6))
        print (dividir (12,6))
        print (multiplicar (5,6))
        print (cuadrado (5))
##FORMA 2 DE IMPORTACIÓN DE ARCHIVOS. 

import OPS.operaciones as OP 
    import OPS.sumar as s
    import OPS.operaciones 
    import OPS.multiplicar

if __name__ == "__main__": 
    print (OP.cuadrado(5))
    print (s.sumar(3,4))
    print (multiplicar (4,5))
```

### CLASE 3. 
### Ejercicio1. 
<div style= "text-align: justify">  Función que reciba el nombre de una persona y el año de nacimiento retornando el mensaje de "hola" nombre, " tienes" edad "años". </div>
<div style= "text-align: justify">   En ésta función, el requerimiento principal es que reciba un nombre, año de nacimiento y año actual, el año de nacimiento se pide para poder sacar el valor de la edad actual. </div>
 <div style= "text-align: justify">  Se muestra de 3 maneras diferentes como se pueden generar tales requerimientos. En las todas las funciones se muestra la lógica de poder arrojar la respuesta, para la edad de la persona;  solamente se deben de asignar funciones y se debe de restar el año de nacimiento con el año actual. </div>


```python
#PRIMERA FORMA DE HACERLO
def nombre_edad (nombre: str, año_nac: int, año_actual: int)-> str: 
    edad=año_actual - año_nac
    return f"hola {nombre},  tienes {edad} años" 
#SEGUNDA FORMA DE HACERLO
def nombre_edad2 (nombre: str, año_nac: int, año_actual: int)-> str: 
     return f"hola {nombre},  tienes {año_actual- año_nac} años"
#FORMA TRES DE HACERLO
def nombre_edad3 (nombre: str, año_nac: int, año_actual: int)-> str: 
     return f"Hola {nombre}, tienes {calcular_edad(año_nac-año_actual)} años"
    
print (nombre_edad("Alba", 2002, 2022))
print (nombre_edad2("Alba", 2002, 2022))
```


### Operaciones básicas. Formas de representar números. 


```python
##NOTACION CIENTIFICA 
numeroPI2 = 314.45896513258
print(f"{numeroPI2: .2e}")

##PORCENTAJE 
numeroporcentaje = 0.25689412654
print(f"{numeroporcentaje:%}")
print (f"{numeroporcentaje:.2%}") ##TE CONVIERTE DE NUMERO DECIMAL A PORCENTAJE Y TE DEJA LOS ULTIMOS DOS DIGITOS DEL DECIMAL

#NUMEROS BINARIOS 
print(f"{25:b}")

#UNICODES 
print (f"{13:c}")

#HEXADECIMAL 
print (f"{255:x}")

##OCTAL 
print(f"{255: o}")

```

### Ejercicio2. 
### FUNCIONES
 <div style= "text-align: justify"> Escriba una función que genere una tabla de multiplicar recibiendo como argumento la cantidad de num  a generar </div> 
<div style= "text-align: justify">  Las funciones son mecanismos que ayudan a la facilitación de procesos dentro de un programa, en éste caso, la función tabla_multi lo que hace es crear un ciclo que permita crear una tabla de multiplicación, donde los argumentos son 2  variables del tipo int, donde una será el total de números a generar y el otro la tabla (ya sea la del 5 o 2), el ciclo for, permite que inicie un contador donde su rango inicia desde el 1 y se va aumetando uno, finalmente se imprimte la variable del rango y se multiplica por la variable 2 que será el operando por el que se generará la tabla (sea 5 o 2).  </div>


```python

def tabla_multi(n= int, n2=int):  ##PRODUCTO 

    for i in range (1, n+1):
     print(i*n2)

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

```

######  ** APRENDIZAJES DENTRO DEL ENTORNO DE PYTHON. REALIZACIÓN Y COMPRENSIÓN DE LISTAS, TUPLAS YSETS (ENTRE OTROS).**

#### LISTAS
### Ejercicio 3. 
### Rellenar una lista con los números naturales del 1 al 10 mediante una lista. 

<div style= "text-align: justify">  Manejo de listas en Python. Se hizo de manera manual, una lista dónde se declara como vacía, posteriormente, se hace un ciclo for donde en rango, se declara el límite que tomará la lista, es decir, dentro de un rango del 0 al 10, donde su inicialización será aparte del 0 y terminará en el 11, éstos rangos son solamente la ubicación de índice donde se almacenarán los números del 1 al 10. Para poder añadiar elementos a una lista, pila o almacenaje se utiliza el método "append" que lo que hace es agregar datos al final de la lista. Finalmente se imprime la lista. </div>


```python

lista_num_naturales =[]
for a in range (0,11): s
    lista_num_naturales.append(a) 
    print(lista_num_naturales)

```

### Listas. Simulación de una base de datos con fstrings.   

  <div style= "text-align: justify">  Dentro del manejo de fstrings en Python, es posible generar una base de datos, en este casp de manera sencilla, la lista se almacena con datos ya dados, las fstrings nos permiten ingresar ciertos parámetros donde se establecen márgenes de la impresión de texto, como es en el caso de la impresión de la base de datos de a continuación--->     </div>


```python

e = ["NOMBRE", "EST DAT", "PROG FUNC", "INGLES"]
alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
m_e_d= (9,8,7,6)
m_e_p= (9,5,9,8)
m_e_f= (9,8,7,6)
m_e_ñ= (9,8,7,6)

print (f"{e[0]:^15}{e[1]:^15}{e[2]:^15}{e[3]:^15}")
for i in range (len(alumnos)): 
    print (f"{alumnos [i]:^15}{m_e_d[i]:^15} {m_e_p[i]:^15} {m_e_f[i]:^15} ")

```

### MANDAR EL REPORTE ANTERIOR A UNA FUNCIÓN (MISMA BASE DE DATOS)


```python

def reporte (msj=int): 
    print (f"{e[0]:^{msj}} {e[1]:^{msj}}{e[2]:^{msj}}{e[3]:^{msj}}")
    for i in range (len(alumnos)): 
        print (f"{alumnos [i]:*^{msj}}{m_e_d[i]:*^{msj}} {m_e_p[i]:*^{msj}} {m_e_f[i]:*^{msj}} {m_e_ñ[i]:*^{msj}}")

if __name__=="__main__": 
    reporte(25)
```

## USO DE LISTAS, MÉTODOS PARA AÑADIR, BORRAR Y DISECCIONAR LISTAS. 
<div style= "text-align: justify"> Dentro del manejo de datos de una lista, se encuentran diferentes formas de poder vibilizar los datos dentro de ésta, existen métodos como los slices, que consiste extraer elementos de la lista, argumentada con límites. en los siguientes códigos se verá con mayor ejemplificación. </div>

### Clase 4 ---> LISTAS. 
 <div style= "text-align: justify"> El manejo de datos dentro de conjuntos de elementos es variable, aparte de las listas, existen los sets y conjuntos, los cuales poseen su sintaxis única, en el caso siguiente, se muestra como se declara una lista con diferentes tipos de datos, en el caso de las listas, éstas pueden almacenar datos de diferente tipo, en el ejemplo se muestra en la lista 2 cómo se guardan dentro de la lista; sets y conjuntos, la diferencia es que los sets se almacenan entre parentesis, y los conjuntos con llaves. </div>


```python
lista1= [1,2,3,4,5] CLASE 4 LISTAS
print (lista1)
lista2= [1, 3.14, "a", True, (1,2,3), {8,"a", 5.4}] ##aqui hay, listas, sets y conjuntos (en ese orden)
print(lista2)

print(len(lista1)) ##LEN, es una funcion que nos dice la cantidad de elementos que hay en el argumento y te lanza un unumero entero ##
print(lista2[2])

lista_cal = []
lista_cal.append(5)
print(lista_cal)
lista_cal.append(8)
print(lista_cal)

```

#### Ejemplo1. 


```python
##SLICES (REBANADAS)
lista1= [1,2,3,4,5,6,7,8,9,10]
print(lista1)
print(lista1[:]) ##imprime exactamente la lista en general 
print(lista1[0:10]) ##imprime lo mismo que la anterior 
print(lista1[int(len(lista1)/2):]) ##imprime la mitad de los elementos de la lista

print(lista1[int(len(lista1)/2)]) 
print(lista1[0:-1])
print(lista1[3:7])
print(lista1[-7:-3])

lista1 =[0,1,2,3,4]
lista2= [5,6,7]
lista1[5:] =[5,6,7] ##manera uno de añadir elementos a una lista 
lista1.append(5) #manera 2 de aladir elementos (recordar que el append añade elementos pero hasta el final)
lista1[len(lista1):] = lista2
print(lista1)

lista1[:0] =lista2 ##Método para insertar los numeros al inicio de la lista
print(lista1)

lista1.append(lista2)
print(lista1)

lista1.extend(lista2)
print(lista1)

# ##COMO BORRAR UN ELEMENTOS EN UNA LISTA 
del (lista1[0])
print(lista1)

# ##BORRAR CON SLICES 
del(lista1[2:5])
print(lista1)
```

### Ejemplo 2. Listas y formas de almacenar sus datos. 


```python

lista1= [1, 'dos',  3, 'cuatro']
print(lista1)
lista2=lista1
print(f"lista 1: {lista1}")
print(f"lista 2: {lista2}")
lista2[1]=lista1
print("________")
print(f"direccion: {id(lista1)}, lista 1: {lista1}")
##AQUI, LO QUE PASA ES QUE LA LISTA 1 NO SE ALMACENA EN ALGUN LADO, POR LO QUE LA DIRECCION ES EXÁCTAMENTE LA MISMA QUE LA LISTA2 
#Y NO HAY UNA LOCALIDAD ÚNICA
print(f"direccion: {id(lista2)}, lista 1: {lista2}")
print("FORMA CORRECTA")
lista1 = [1, "dos", 3, "cuatro"]
lista2=lista1[:]
print(f"direccion lista1: {id(lista1)}") ##Pero aqui, existe un almacenamiento donde cada lista tiene su propio espacio, por lo que los datos de cada uno se queda intactos 
print(f"direccion lista2: {id(lista2)}")
```

###  Listas. Ejemplos y ejercicios. -->SETS, TUPLAS, DICCIONARIOS--<

  <div style= "text-align: justify"> Los sets o conjuntos se utilizan para almacenar múltiples elementos en una sola variable.
Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos. 
Las tuplas son un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas. Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía. En el siguiente código se muestran unas ejemplificaciones de lo que es: </div> 

### Ejemplo 1. 


```python
#LISTA PRINCIPAL DEL EJERCICIO: 
alumnos = ["Hugo", "Paco", "Luis", "Lupita"] 

#LISTAS
print(f"Alumnos:  {alumnos}")

for i in range (len (alumnos)): 
    print (f"Alumnos: {alumnos[i]}")

#TUPLAS 
for i in range (len (alumnos)): 
    print (f"Alumnos: { i + 1}: {alumnos[i]}")

# #SETS 
alumnos = {"Hugo", "Paco", "Luis", "Lupita"}
print (f"Alumnos: {alumnos}")

# #DICCIONARIOS 
alumnos={"Nombre": "Hugo", "materia1": 10, "Materia2": 5 }
print(f"Alumnos: {alumnos}")
print(f"Alumno: {alumnos ['nombre']}")


#lISTAS A SETS 
numeros_list = (1,2.3,1,1,2,2,2,3,3,4,5,7,8,8,9,9)
numeros_sets = {1,2.3,1,1,2,2,2,3,3,4,5,7,8,8,9,9}

print(numeros_list)
print (numeros_sets)
```
