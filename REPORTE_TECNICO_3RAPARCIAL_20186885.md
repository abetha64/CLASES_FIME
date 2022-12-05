# UNIVERSIDAD DE COLIMA 
## FACULTAD DE INGENIERÍA MECÁNICA Y ELÉCTRICA
### INGENIERÍA EN COMPUTACIÓN INTELIGENTE.
#### Profesor: Walter Alexander Mata López 
#### Alumna: Alba Beth-birai López Aguilar 20186885



### ** TEMAS VISTOS EN LA PARCIAL ** ###
#### FUNDAMENTOS DE LA PROGRAMACION ORIENTADO DENTRO DE LOS LENGUAJES:
#### ***ELIXIR ***
####  __-ERLANG__ 


 <div style= "text-align: justify"> En la programación funcional, se encuentran diferentes paradigmas de programacion, en la cual se considera el cómputo como la evaluacion de funciones matemáticas que ayudan a evitar el cambio de estado y los datos iterables (o mutables). Existen dentro de ésta, se haya la programacion de manera estructurada o procedural, donde están los lenguajes tales: C, PASCAL, COBOL etc </div>

# ELIXIR 
- Elixir es un lenguaje dinamico. 

 </div>  <div style= "text-align: justify"> En Elixir, se pueden hacer sin fin de cosas, este lenguaje tiene la capacidad de un lenguaje funcional, es decir, su sintaxis es de tipo imperativo, lo que significa que no necesita dar la instrucción en concreto para que el programa lo haga, es necesario solamente, escribir la palabra reservada y así invocar lo que se solicita. </div> 

<div style= "text-align: justify"> Para la utilización del lenguaje, se manejó el Shell, en ésta, se pueden realizar expresiones que evaluan al presionar, se pueden escribir múltiples expresiones, retornando siempre el último valor calculado. Cabe destacar que dentro del Shell, no se almacena dato alguno, es decir, si se sobrecarga una nueva variable, el valor anterior al nuevo deja de existir y se retorna el ultimo almacenado. </div>  

## Variables
- No es necesario declarar de manera explícita una variable o su tipo de dato. 
- El tipo de dato se determina de acuerdo al valor contenido 
- La asignación se conoce como fijación (binding)  
- Cuando se inicializa una variable con un valor, la variable se fija con ese valor.

### Características
- El nombre de una variable siempre inicia con un caracter alfabetico en minus o subrayado. 
- Tras ésto, puede llevar cualquier combinación de caracteres. 
- Puede terminar con los caracteres ? o !
- Los datos datos son inmutables, es decir, su contenido no puede cambiarse
- Las variables pueden ser refijadas a un diferente valor 

### Módulos y funciones
#### Módulos
- Un módulo consta de varias funciones
- Cada función debe de estar definida dentro de un módulo 
- El IO permite varias operaciones, la función *puts* permite imprimir un mensaje en pantalla
- Un módulo puede estar dentro de un archivo, y un archivo puede tener varios módulos.

_REGLAS DE LOS MÓDULOS_
* Inicia con una letra minúscula 
* Se escribe con el estilo CamelCase
* Puede consistir en caracteres alfanuméricos, subrayados y puntos



#### Funciones 
- Siempre debe de estar dentro de un módulo
- Los nombres de las funciones son iguales que las variables 
- Pueden terminar con los carateres ? o !.
- Por convención el ? se utiliza cuando la función retorna true o false
- El ! se utiliza generalmente en funciones que podrían provocar algún error
en tiempo de ejecución
- Tanto *defmodule* como *def* NO son palabras reservadas del lenguaje, son
macros

### SINTAXIS GENERAL 
– *NombreModulo.nombre_funcion(args)*

## ESTRUCTURA DEL CÓDIGO EN ELIXIR 
####  Aridad (Arity) de funciones 
- Nombre para el número de argumentos que una función recibe 
- Una función se identifica por: 
1. El módulo donde se encuentra 
2. Su nombre 
3. Su aridad 
#### Polimorfismo (sobrecarga)
- Dos funciones con el mismo nombre pero con diferente aridad son 2 diferentes funciones

#### Atoms
- Constantes literales nombradas 
- Es una constante cuyo nombre es su propio valor 
- Inician con : (2 puntos)
- Seguidos de caracteres alfanuméricos y/o subrayados 
- Se pueden usar espacios en blanco si se ponen entre comillas 

Un Atoms consta de 2 partes: 
1. **Texto**: el que se pone después de los 2 puntos 
2. **Valor**: Es la referencia a la tabla de atoms 

- Un atom se pueden nombrar con mayus inicial 
- Atoms como booleanos
- Los valores booleanos son atoms

#### Atoms *nil* *null* *false*
- Los atoms *nil* y *false* son tratados como valores falsos, mientras que todo lo demás es tratado como un valor de verdad
- Esta propiedad es útil con los operadores de cortocircuito: 
1. || -> retorna la primera expresión verdadera
2. && -> retorna la segunda siempre y cuando la primera lo sea también
3. ! -> retorna la negación de la expresión sin importar el tipo de dato



```python

#EJEMPLO DE UNA FUNCION

defmodule HolaMundo do
    def mensaje do
    IO.puts("Hola Mundo")
    end
end
```

 * EJEMPLO DE UNA FUNCIÓN CON ARGUMENTOS EN LENGUAJE DE ELIXIR*


```python
defmodule Calculadora do
    def suma(n1,n2) do
        n1 + n2
    end
end
```

* EJEMPLO DE UN ARCHIVO CON VARIOS MÓDULOS.* 


```python
defmodule Calculadora do ///#MODULO 1
    def suma(n1,n2) do
        n1 + n2
    end
end

defmodule Areas do ///#MODULO 2
    def area_cuadrado(l) do
        l*l
    end
end
```

* FUNCIONES DE MANERA CONDENSADA *


```python
defmodule Geometria do
    def perimetro_cuadrado(l), do: 4*l
    def perimetro_rectangulo(l1,l2), do: 2*l1 + 2*l2
end
```

 _VISIBILIDAD DE FUNCIONES_
- Se pueden utilizar funciones privadas con el constructor *defp*
- Función pública y privada



```python
defmodule TestPublicoPrivado do
    def funcion_publica(msg) do
        IO.puts("#{msg} publico")
        funcion_privada(msg)
    end
    
    defp funcion_privada(msg) do
        IO.puts("#{msg} privado")
    end
end

TestPublicoPrivado.funcion_publica("este es un mensaje")
```

Módulo Geometría


```python
defmodule Geometria do
    def perimetro1(l), do: cuadrado(l)
    def perimetro2(l), do: Geometria.cuadrado(l)
    defp cuadrado(l), do: 4*l
end
```

* CODIGO DE EJEMPLO DE EJERCICIO EN ELIXIR 


```python
defmodule Operaciones do
    def suma(n1,n2), do: n1 + n2
    def cuadrado(n), do: n * n
end

defmodule Test do
    def start do
        4 |> Operaciones.suma(5) |>Operaciones.cuadrado
    end
end
```

* EJEMPLO DE POLIMORFISMO


```python
defmodule Rectangulo do
    def area(l) do
        l * l
end

def area(l1,l2) do
    l1 * l2
    end
end
```

* EJEMPLO DE POLIMORFISMO CON UNA CALCULADORA 

En este módulo genera 2 funciones como en el codigo anterior, se puede utlizar combinación de argumentos por defecto


```python
defmodule Calculadora do
    def suma(n) do
      suma(n,0)
end

def suma(n1,n2) do
   n1 + n2
  end
end
```

#### IMPORTS
- Creamos un archivo fuente *main.ex*
- Escribimos el siguiente código:


```python
import ModuloImportado

defmodule ModuloMain do
  def main do
   IO.puts("Funcion main")
   funcion_importada("Esta funcion es importada")
  end
end
```

- Se crea el módulo a importar *modsec.ex
- Escribimos el siguiente código:


```python
defmodule ModuloImportado do
    def funcion_importada(msg) do
    IO.puts(msg)
    end
end
```

Si no se requiere importar el módulo, se puede utilizar de manera directa indicando el módulo y la función, esto es: 
Y es necesario volver a compilar la función *main*


```python
defmodule ModuloMain do
    def main do
        IO.puts("Funcion main")
        ModuloImportado.funcion_importada("Esta funcion es importada")
    end
end
```

### ALIAS 
- Se puede utilizar *alias* como alternativa a *import*, permite hacer una referencia a un módulo con otro nombre


```python
defmodule ModuloMain do
    alias ModuloImportado, as: MI
        
    def main do
     IO.puts("Funcion main")
     MI.funcion_importada("Esta funcion es importada con alias")
    end
end
```

#### ATRIBUTOS DE MÓDULO 
- Existen los atributos en tiempo de compilación (mientras están cargados)



```python
defmodule Geometria do
    @pi 3.141592
    def area(r) do
     r*r*@pi
    end
    
    def circunferencia(r) do
      2 * r * @pi
    end
end
```

### TIPOS DE DATOS 
- Elixir utiliza el mismo sistema de tipos de Erlang
1. Los números (*numbers*) pueden ser enteros o flotantes
2. Integer 


```python
iex> is_integer(3)
true
iex> is_float(3)
false
iex> i 34 #inspect
Term
34
Data type
Integer
```

3. Float 


```python
iex> is_integer(3.5)
false
iex> is_float(3.5)
true
iex> i(3.5)
Term
3.5
Data type
Float
Reference modules
Float
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```

4. Notación científica


```python
iex> 3.25555e-3
0.00325555
iex> 3.25555e3
3255.55
iex>i 3.25555e3
Term
3255.55
Data type
Float
Reference modules
Float
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```

5. Operaciones aritméticas


```python
iex> 5 * 4 / 3 + 2 - 5
3.666666666666668
iex> 5/4
1.25
iex> 5/5
1.0
iex> div(5,5)
1
iex> rem(5,5)
0
```

#### Tuplas 
- Son como estructuras o registros
- Permiten agrupar elementos fijos 

Para extraer elementos se usa la función *elem*


```python
iex> nombre = elem(persona, 0)
"Alex"
iex> nombre
"Alex"
iex> edad = elem(persona,1)
49
iex> edad
49
```

Para modificar un elemento se usa la función *put_elem*


```python
iex> put_elem(persona,0,"Alexander")
{"Alexander", 49}
```

Las tuplas son inmutables, por lo que se modifica
Si se necesita cambiar , hay que almacenar el cambio en otra variable, o en la misma si ya no se desea conservar los valores. 

####   LISTAS 
- Manejo dinámico de datos 
- Funcionan como listas enlazadas simples



```python
iex> numeros_pares = [2,4,6,8,10]
[2, 4, 6, 8, 10]
iex> i [2, 4, 6, 8, 10]
Term
[2, 4, 6, 8, 10]
Data type
List
Reference modules
List
Implemented protocols
Collectable, Enumerable, IEx.Info, Inspect, List.Chars, String.Chars
iex> length(numeros_pares)
5
```

- Insertar un elemento 


```python
iex> numeros_pares
[2, 4, 6, 8, 12]
iex> numeros_pares = List.insert_at(numeros_pares,4,10)
[2, 4, 6, 8, 10, 12]
iex> numeros_pares = List.insert_at(numeros_pares,-1,14)
[2, 4, 6, 8, 10, 12, 14]
```

- Concatenar dos listas


```python
iex> numeros_naturales = [1,2,3,4] ++ [5,6,7,8]
[1, 2, 3, 4, 5, 6, 7, 8]
iex> numeros_naturales
[1, 2, 3, 4, 5, 6, 7, 8]
```

### Recursion sobre listas
- El formato de una lista es [head | tail]
- head puede ser de cualquier tipo
- tail siempre es una lista
- si tail es una lista vacía [], indica que es el final de la lista.


```python
iex> []
[]
iex> [1|[]]
[1]
iex> [1|[2|[]]]
[1, 2]
iex> [1|[2|[3|[]]]]
[1, 2, 3]
iex> [1|[2|[3|[4|[]]]]]
[1, 2, 3, 4]
iex> [1|[2,3,4]]
[1, 2, 3, 4]
```

#### MAPAS 
- Par llave-valor 
- Pueden ser cualquier término 



```python
iex> persona = %{:nombre => "Alex", :edad => 49, :trabajo =>"profesor"}
%{edad: 49, nombre: "Alex", trabajo: "profesor"}
iex> persona
%{edad: 49, nombre: "Alex", trabajo: "profesor"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be"
}
%{b: "be", m: "eme", x: "equis", z: "zeta"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be"
, :n => "ene"}
%{b: "be", m: "eme", n: "ene", x: "equis", z: "zeta"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be"
, :n => "ene", :a => "aaaa"}
%{a: "aaaa", b: "be", m: "eme", n: "ene", x: "equis", z: "zeta"}
```

###  Binaries 
- Un binary es un grupo de bytes 
- Cada número representa un valor que corresponde a un byte 
- Cualquier valor mayor a 255 se trunca al valor en byte 


```python
iex(14)> <<1,2,3,4,5>>
<<1, 2, 3, 4, 5>>
iex> <<255>>
<<255>>
iex> <<256>>
<<0>>
iex> <<257>>
<<1>>
iex> <<512>>
<<0>>
```

#### Strings (Binary String)
- No existe un tipo String dedicado 
- Los Strings se representan como binary o list 
- Lo más sencillo es usar sobles comillas
- Se pueden insertar expresiones en las cadenas (interpolación de cadena) mediante #{}


```python
iex> "El cuadrado de 2 es #{2*2}"
"El cuadrado de 2 es 4"
```

#### Patter Matching 
- Operador  pin ^ 
- Evita la refijación  (rebind)


```python
iex> x = 3
3
iex> 3 = x
3
iex> 5 = x
** (MatchError) no match of right hand side value: 3
iex> x = 5
5
iex> x
5
iex> ^x = 5
5
iex> ^x = 10
** (MatchError) no match of right hand side value: 10
iex> 10 = x
** (MatchError) no match of right hand side value: 5
```


```python
// Tuplas
iex> leer_archivo_ok = {:ok, "texto del archivo"}
{:ok, "texto del archivo"}
iex> leer_archivo_error = {:error, "No se pudo leer el archivo"}
{:error, "No se pudo leer el archivo"}
iex(8)> {:ok, respuesta} = leer_archivo_ok
{:ok, "texto del archivo"}
iex(9)> respuesta
"texto del archivo"
iex(10)> {:error, respuesta} = leer_archivo_error
{:error, "No se pudo leer el archivo"}
iex(11)> respuesta
"No se pudo leer el archivo"
```


```python
///Listas

iex> [head | tail] = [1,2,3,4]
[1, 2, 3, 4]
iex> head
1
iex> tail
[2, 3, 4]
iex> [head | _] = [1,2,3,4]
[1, 2, 3, 4]
iex> head
1
iex> [_ | tail] = [1,2,3,4]
[1, 2, 3, 4]
iex> tail
[2, 3, 4]
iex> mi_lista = [1,2,3,4]
[1, 2, 3, 4]
iex> [1,2,x,4] = mi_lista
[1, 2, 3, 4]
iex> x
3
```

#### GUARDAS


```python
defmodule Numero do
    def cero?(0), do: true
    def cero?(n) when is_integer(n), do: false
    def cero?(_), do: "No es entero"
end

IO.puts(Numero.cero?(0))
IO.puts(Numero.cero?(2))
IO.puts(Numero.cero?("3"))
```

### CONDICIONALES 
- If 


```python
defmodule Persona2 do
    def sexo(sex) do
        if sex == :m do
            "Masculino"
            else if sex == :f do
                "Femenino"
            else
            "Sexo desconocido"
            end
        end
    end
end
```


```python
defmodule Persona1 do  ###FORMA 1
    def sexo(sex) do
        if sex == :m do
            "Masculino"
        else
            "Femenino"
        end
    end
end
```

### CASE 


```python
defmodule Persona3 do
    def sexo(sex) do
        case sex do
            :m -> "Masculino"
            :f -> "Femenino"
             -> "Sexo desconocido"
        end
    end
end
```

### MATCH CON FUNCIONES 


```python
defmodule Persona5 do
    def sexo(sex) when sex == :m, do: "Masculino"
    def sexo(sex) when sex == :f, do: "Femenino"
    def sexo(_sex), do: "sexo desconocido"
end
```

COND 


```python
defmodule Persona6 do
    def sexo(sex) do
        cond do
            sex == :m -> "Masculino"
            sex == :f -> "Femenino"
            true -> "Sexo desconocido"
        end
    end
end
```

## HERRAMIENTA MIX
- Es una herramienta de la línea de comandos CLI, permite:
1. Crear proyectos de Elixir 
2. Mantenerlos 
3.  Proporciona tareas para: 
- Documentar 
- Compilar
- Depurar 
- Probar (test)
- Manejar dependencias


```python
##CREAR PROYECTOS

C:\>mix new calculadora
* creating README.md
* creating .formatter.exs
* creating .gitignore
* creating mix.exs
* creating lib
* creating lib/calculadora.ex
* creating test
* creating test/test_helper.exs
* creating test/calculadora_test.exs
Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:
cd calculadora
mix test
Run "mix help" for more commands.
C:\>
```

- CARGA DE UNA APLICACION 


```python
// Ingresar al directorio dondese creo la nueva aplicación
C:\>cd calculadora
C:\calculadora>
```

- Lanzar el shell de Elixir con mix 


```python
Compiling 1 file (.ex)
Generated calculadora app
Interactive Elixir (1.10.4) - press Ctrl+C to exit (type h() ENTER for he
lp)
iex(1)>
```

- Ejecutar la función hello ()


```python
iex(1)> Calculadora.hello()
:world
iex(2)>
```

- Documentación con ExDoc
 1. Abrir el archivo mix.exs
 2. Modificar las dependencias agregando {:ex_doc, “~>0.12”}


```python
defp deps do
    [
        {:ex_doc, "~>0.12"}
    ]
end
```

- Ejecutar el comando *mix deps.get*


```python
C:\calculadora>mix deps.get
Resolving Hex dependencies...
Dependency resolution completed:
New:
earmark_parser 1.4.12
ex_doc 0.23.0
makeup 1.0.5
makeup_elixir 0.15.0
nimble_parsec 1.1.0
* Getting ex_doc (Hex package)
* Getting earmark_parser (Hex package)
* Getting makeup_elixir (Hex package)
* Getting makeup (Hex package)
* Getting nimble_parsec (Hex package)
C:\calculadora>
• Ejecutar mix docs
C:\calculadora>mix docs
==> earmark_parser
Compiling 1 file (.yrl)
Compiling 2 files (.xrl)
Compiling 3 files (.erl)
Compiling 32 files (.ex)
Generated earmark_parser app
==> nimble_parsec
Compiling 4 files (.ex)
Generated nimble_parsec app
==> makeup
Compiling 44 files (.ex)
Generated makeup app
==> makeup_elixir
Compiling 6 files (.ex)
Generated makeup_elixir app
==> ex_doc
Compiling 22 files (.ex)
Generated ex_doc app
==> calculadora
Compiling 1 file (.ex)
Generated calculadora app
Generating docs...
View "html" docs at "doc/index.html"
View "epub" docs at "doc/calculadora.epub"
C:\calculadora>
```

Test 
• Se realiza a partir del script del test


```python
C:\calculadora>mix test
Compiling 1 file (.ex)
Generated calculadora app
..
Finished in 0.07 seconds
1 doctest, 1 test, 0 failures
Randomized with seed 954000
```

Doctest
• Se realiza a partir de la documentación de las funciones


```python
defmodule Matematicas do
    def calculadora(opcion,{n1,n2}) do
        case opcion do
            "+" -> n1+n2
            "-" -> n1-n2
            "/" when n2 != 0 -> n1/n2
            "/" when n2 == 0 -> "No se puede dividir por 0"
            "*" -> n1*n2
            _ -> :error
        end
    end
end

IO.inspect Matematicas.calculadora("+",{5,4})
IO.inspect Matematicas.calculadora("-",{5,4})
IO.inspect Matematicas.calculadora("/",{5,4})
IO.inspect Matematicas.calculadora("/",{5,0})
IO.inspect Matematicas.calculadora("*",{5,4})
```

Cond


```python
defmodule DiaSemana do
    def dia(d) do
        cond do
            d == 1 -> "Lunes"
            d == 2 -> "Martes"
            d == 3 -> "Miercoles"
            d == 4 -> "Jueves"
            d == 5 -> "Viernes"
            d == 6 -> "Sabado"
            d == 7 -> "Domingo"
            true -> "Dia no valido"
        end
    end
end

IO.puts DiaSemana.dia(1)
IO.puts DiaSemana.dia(2)
IO.puts DiaSemana.dia(3)
IO.puts DiaSemana.dia(4)
IO.puts DiaSemana.dia(5)
IO.puts DiaSemana.dia(6)
IO.puts DiaSemana.dia(7)
IO.puts DiaSemana.dia(8)
```

UNLESS


```python
defmodule MayorDeEdad do
    def mayor1(edad) do
        unless edad >= 18 do
            "Es menor de edad"
        end
    end
end
```

### FUNCIONES ANÓNIMAS
- No tienen nombre
- Se pueden fijar a variables


```python
defmodule Calculadora do
    def suma(n1,n2), do: n1+n2
end
suma_anonima = fn(n1,n2) -> n1 + n2 end

IO.puts(Calculadora.suma(5,4))
IO.puts(suma_anonima.(5,5))
>elixir main.ex
9
10
```

## Operador Pipe
- Dada una listra con n numeros, se desea obtener el cuadrado de la suma de los elementos de la cola. Si la lista es (1,2,3,4) el resultado es (2+3+4+5)^2 



```python
sum = 0
lista = [1,2,3,4,5]
lista = tl(lista)
IO.inspect(lista)
[num|lista] = lista
#para sacar el 2
IO.inspect(num)
IO.inspect(lista)
sum = sum + num
IO.inspect(sum)
#para sacar el 3
[num|lista] = lista
IO.inspect(num)
IO.inspect(lista)
sum = sum + num
IO.inspect(sum)
#para sacar el 4
[num|lista] = lista
IO.inspect(num)
IO.inspect(lista)
sum = sum + num
IO.inspect(sum)
#para sacar el 5
[num|lista] = lista
IO.inspect(num)
IO.inspect(lista)
sum = sum + num
IO.inspect(sum)
IO.puts("EL resultado es: #{sum*sum}")
```

* EJEMPLO  DE TEST PIPE


```python
defmodule PipeTest do
    def cuadrado(n), do: n*n
        
    def suma(lista) do
      Enum.sum(lista)
    end
end

IO.puts("#{PipeTest.cuadrado(PipeTest.suma(tl([1,2,3,4,5])))}")
```

###  HERRAMIENTA DE DEPURACIÓN (DEBUGGING)


```python
ddefmodule PipeTest do
    def cuadrado(n), do: n*n
        
    def suma(lista) do
      Enum.sum(lista)
    end
    
    def csc(lista) do
      lista
      |> tl
      |> IO.inspect
      |> suma
      |> IO.inspect
      |> cuadrado
    end
end

IO.puts("#{PipeTest.csc([1,2,3,4,5])}")
```

#### Loops y recursión (RANGOS)

* Representan una secuencia de números 
* Se definen con un límite inferior y límite superior
* Son inclusivos
* Se separan con 2 puntos (..)
* Son equivalentes a una lista:  – 1..10 -> [1,2,3,4,5,6,7,8,9,10]
* Es más eficiente que una lista de números secuenciales, puesto que solose almacenan 2 enteros, el deliniciop y el del final 
* Son enumerables, cada número segenera conformese itere sobre el rango 
* La función  *Enum* puede usarse con rangos 




```python
iex> 1..01
1..1
iex> 1..10
1..10
iex> li..ls = 1..10
1..10
iex> li
1
iex> ls
10
iex> li = 10
10
iex> ls = 20
20
iex> li..ls
10..20
iex> ls..li
20..10
```


```python
###Se puede generar una lista a partir de un rango

iex> Enum.to_list(1..10)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iex> Enum.to_list(10..1)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
• Contar cuantos elementos hay en el
```


```python
###Contar cuantos elementos hay en el rango
iex> rango = 10..25
10..25
iex> Enum.count(rango)
16
```


```python
###Determinar si un elemento x se encuentra dentro del rango
iex> rango = 10..25
10..25
iex> Enum.member?(rango,9)
false
iex> Enum.member?(rango,20)
true

###otra forma de saberlo es con el operador in
iex> 9 in rango
false
iex> 20 in rango
true
```

#### FUNCIONES DE *ENUM*


```python
###Contar del 1 al 10

for x <- 1..10 do
IO.puts(x)
end
```


```python
###Al saber que lo que genera es una lista, se puede utilizar la función sum del
###módulo Enum

sum = for x <- 1..10 do
    x
end

IO.puts Enum.sum(sum)
```

### EJERCICIOS DE RECURSIÓN.  
HACER UN PROGRAMA RECURSIVO QUE IMPRIMA *n* VECES UN MENSAJE 


```python
defmodule Repetir do
    def imprimir(msg, n) when n<= 1 do
       IO.puts("#{n}: #{msg}")
    end
    
    def imprimir(msg, n) do
      IO.puts("#{n}: #{msg}")
      imprimir(msg, n-1)
    end
end

Repetir.imprimir("Hola",10)
```


```python
### Invertir el orden de los números

defmodule Repetir do
  def imprimir(msg, n,ls) when n>= ls do
    IO.puts("#{n}: #{msg}")
  end

    def imprimir(msg, n,ls) do
      IO.puts("#{n}: #{msg}")
      imprimir(msg, n+1,ls)
    end
end

Repetir.imprimir("Hola",1,10)
```

####  Escribir un programa recursivo que sume todos los elementos de una serie de números en una lista 



```python
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
      sum_list(tail, suma+head)
    end
end

IO.puts(Matematicas.sum_list([1,2,3,4,5,6,7,8,9,10],0))
IO.puts(Matematicas.sum_list([1,3,5,7,9,10,15],0))
```

#### Obtener el promedio de 10 calificaciones entre 0 y 10 almacenadas en una lista


```python
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
      sum_list(tail, suma+head)
    end
end
IO.puts(Matematicas.sum_list([10,5,9,9,8,5,7,9,6,5],0)/10)
```

#### Crear una función promedio que calcule el promedio de 10 calificaciones almacenadas en una lista entre 0 y 10


```python
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
     sum_list(tail, suma+head)
    end

    def promedio(calificaciones, n) do
      sum_list(calificaciones,0)/n
    end
end
IO.puts(Matematicas.promedio([10,5,9,9,8,5,7,9,6,5],10))
```

#### Calcular el promedio de n calificaciones entre 0 y 10 en una lista


```python
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
      sum_list(tail, suma+head)
    end
    
    def promedio(calificaciones) do
      sum_list(calificaciones,0)/Enum.count(calificaciones)
    end
end
IO.puts(Matematicas.promedio([10,5,9,9,8,5,7,9,6,5]))
```

#### Escriba el problema anterior con un módulo y una función, recibiendo como argumentos la cantidad de calificaciones a generar, así como el rango de calificaciones.


```python
defmodule Estadistica do
    def promedio(max_cal, _li, _ls) when max_cal <= 1 do
      :error
    end
    def promedio(max_cal, li, ls) when max_cal > 1 do
      calificaciones = for _x <- 1..max_cal do
        Enum.random(li..ls)
       end
       Enum.sum(calificaciones)/Enum.count(calificaciones)
    end
end

IO.puts Estadistica.promedio(50,1,15)
IO.puts Estadistica.promedio(-5,1,15)
```

#### Hacer un programa recursivo que cuente de manera creciente de li (límite inferior) a ls (límite superior) para li>=ls inclusive


```python
defmodule For_range do
    def for_to(n,ls) when n > ls do
        IO.puts "error"
    end
    
    def for_to(n,ls) when n >= ls do
        IO.puts n
    end
    
    def for_to(n,ls) do
        IO.puts n
        for_to(n + 1,ls)
    end
end
IO.puts("Contar de 1 a 10")
For_range.for_to(1,10)

IO.puts("Contar de 12 a 5")
For_range.for_to(12,5)
```

#### Programa que sume los valores de los números consecutivos entre li y ls inclusive


```python
defmodule For_range do
    def for_to(n,ls) when n >= ls do
        n
end

    def for_to(n,ls) do
        n + for_to(n + 1,ls)
    end
end
IO.puts("suma de los numeros de 1 a 10")
IO.puts For_range.for_to(1,10)

IO.puts("suma de los numeros 5 a 12")
IO.puts For_range.for_to(5,12)
```
