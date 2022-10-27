# UNIVERSIDAD DE COLIMA # 
## FACULTAD DE INGENIERIA MECANICA Y ELECTRICA 
#### Carrera: INGENIERIA EN COMPUTACION INTELIGENTE 
#### Alumno: Alba Beth-birai Lopez Aguilar 

<div style= "text-align: justify"> OBJETIVOS DE LA MATERIA: 
  Poder desarrollar y manejar de manera básica el lenguaje DART </div>

### CLASE 1. TIPO DE DATOS

  <div style= "text-align: justify"> DART 
Lenguaje de programacion orientada a objetos, lenguaje de tipo estático, es decir, una vez estructurado no se puede modificar de nuevo </div>

###  TIPO DE DATOS
<div style= "text-align: justify">  >> STRINGS: Representa un conjunto de caracteres. 
 </div> 

 <div style= "text-align: justify"> >> NUM: En Dart,-num- se usa para representar en literales numéricas.   </div>


<div style= "text-align: justify"> >> INT: Aquellos numeros que son solamente de tipo entero.  </div> 

<div style= "text-align: justify"> >> DOUBLE: Aquellos numeros que son de tipo decimal. </div>
 


 <div style= "text-align: justify"> >>Dynamic:  Nos permite declarar una variable en la que el tipo puede cambiar en tiempo de ejecución y puede ser definida de la siguiente forma:  </div> 


```python

//   num numero1 = 5;  <<-VARIABLES DE TIPO NUM
//   print(numero1);
//   num numero2 = 9.81;
//   print(numero1 *numero2);
  
//   dynamic variable ="HOLA";  <<-VARIABLES DE TIPO DINAMIC 
//   print(variable); 
//   dynamic variable1 =5; <<-VARIABLES DE TIPO DINAMIC 
//   print(variable1); 
//   dynamic variable2 =9.81;  <<-VARIABLES DE TIPO DINAMIC 
//   print(variable2); 
//   variable = true; 
// print(variable +  variable2);

 bool esPar(int num){
    if (num % 2 == 0) {
     return true; 
  } else {
    return false; 
  }
```

En el codigo anterior se visualiza la representacion de como imprimir datos con diferente tipado, al ultimo se encuentra una funcion que es de tipo boleano y regresa un valor con cierta cantidad de ceros. 

### EJERCICIOS:
#### CREAR UNA CALCULADORA: SUMA, RESTA, MULTI, DIV. USANDO FUNCIONES Y DECLARACION DE VARIABLES. 


```python
import 'dart:io';
//calculadora que lea dos numeros del teclado y obtenga suma, resta, multiplicación y
//division, usando funciones y asingnado valores a dos variables

void main() {
  int num1 = leerNumero("Dame el primer número");
  int num2 = leerNumero("Dame el segundo número");
  print("${calculadora("x", num1, num2)}");
}

int leerNumero(String mensaje) {
  print(mensaje);
  int num = int.parse(stdin.readLineSync()!);
  return num;
}

String calculadora(String op, int n1, int n2) {
  if (
if (op == "+") {
    return "$n1 + $n2 = ${suma(n1, n2)}";
  } else if (op == "-") {
    return "$n1 - $n2 = ${suma(n1, n2)}";
  } else if (op == "*") {
    return "$n1 * $n2 = ${suma(n1, n2)}";
  } else if (op == "/") {
    return "$n1 / $n2 = ${suma(n1, n2)}";
  } else {
    return "Operación inválida";
  }
}

int suma(int num1, int num2) => num1 + num2;
int resta(int num1, int num2) => num1 - num2;
int multi(int num1, int num2) => num1 + num2;
int divi(int num1, int num2) {
  return num1 + nu
m2;
}
int suma(int num1, int num2) => num1 + num2;
int resta(int num1, int num2) => num1 - num2;
int multi(int num1, int num2) => num1 + num2;
int divi(int num1, int num2) {
  return num1 + num2;
}

```

### CLASE 2. LISTAS Y SISTEMAS NUMÉRICOS EN DART. 
#### LISTAS
<div style= "text-align: justify">  En Dart, la palabra reservada VAR una expresión para referirse a que nuestra variable es de tipo cualquiera. En el codigo siguiente, es visto qué la lista de nombre "miLista" su tipo de dato es "var", por lo que recoge el valor que se ingrese  dentro de la lista, haciendo incapié que una lista puede almacenar caulquier tipo de datos.  </div>


```python
// LISTAS 
var miLista= [1, "HOLA", 9.8, true]; 
 print (miLista); 
//   //AGREGAR ELEMENTOS A UNA LISTA 
 miLista.add(3.1416); 
  print(miLista); 
  
  final miLista = const [1,2,3,4]; 
  print(miLista); 
  var name = "LISTA"; 
  for (var i = 0; i < miLista.length; i++) {
  stdout.write("$i: ${miLista[i]}\n "); 
  }
  
```

### SISTEMAS NUMÉRICOS. 

### OPERADORES DE DECREMENTO Y INCREMENTO


```python
//BINARIO 
print(125.toRadixString(2)); 
//OCTAL
print(125.toRadixString(8));
//HEXDECIMAL 
print(125.toRadixString(16)); 
 var numero =0xFFFF; 
print (numero.runtimeType); 
```


```python
contador = contador +1;  ///Diferentes maneras de usar el incremento en una variable. 
    print(contador); 
contador++; 
    print(contador); 
++contador; 
    print(contador); 
contador+=2;  
    print(contador); 
```

### Diferentes formas de realizar operaciones aritmeticas. 


```python
var n1=15; 
var n2=7; 

print("SUMA: $n1 + $n2 = ${n1 + n2}");
print("RESTA: $n1 - $n2 = ${n1 - n2}");
print("MULTI: $n1 * $n2 = ${n1 * n2}");
print("DIVISION: $n1 / $n2 = ${n1 / n2}");
print("DIVISION: $n1 ~/ $n2 = ${n1 ~/ n2}");
print(pow(5,3));
print("Mínimo: ${min(5,3)}");
print("Máximo: ${max(5,3)}");
print("Seno: ${sin(45*pi/180)}");
```

### CLASE 3
#### CLASES E INSTANCIAS. 
<div style= "text-align: justify"> Clase: Es la parte de un programa donde sealmacenan todas las propiedades, objetos que sevan a utilizar y se realizan los métodos a elección. Una instancia es una copia de una clase.  </div> 


```python
void main(){
   var usuario1= user(); //instancia de la clase user 
   usuario1._nombre ="Alba"; 
   usuario1._edad = 50; 
   usuario1.reporte(); 
    var estudiante1 =estudiante(); 
    estudiante1.name_carrera ="INGENIERIA EN COMPUTACION INTELIGENTE";
    estudiante1.num_cuenta ="20186885"; 
    estudiante1.semestre= 3; 
   estudiante1.reporte(); 
}
```


```python
class user { ////CLASE LLAMADA USER
   String? _nombre; //PROPIEDADES
   int?  _edad; //cuando se pone el guion bajo, es de propiedad privada (solamente la puede usar el programador )
   //MÉTODOS 
     void reporte (user) {
     print(usuario1.nombre); 
     print(usuario1.edad); 
}
```

###  Prodiedades privadas. Métodos de Setter y Getters, Constructores y Mixting. 

<div style= "text-align: justify"> Dentro de la programacion orientada a objetos, y la creacion de clases, existe la posibilidad donde se acceda a ciertas propiedades pero no de manera global, estas propiedades son llamadas de caracter privado, es decir; Son propiedades que solo pueden ser usadas dentro de la clases (de forma interna), la misma se logra colocando UNDERSCORE antes del nombre de la variables. Dentro de la sintaxis se especifica una propiedad privada con el guin bajo  </div> 

###  EJERCICIO 1. 
 ELABORAR UNA CLASE DONDE SE LLAME ESTUDIANTE Y TENGA NUMERO DE CUENTA, NOMBRE DE CARRERA, SEMESTRE


```python

// class estudiante(){
//    String? num_cuenta; <<-SE LE PONE EL SIGNO DE INTERROGACION PARA PODER DECIR QUE ES DE VALOR NULO.
//    String? name_carrera; 
//    int? semestre;  

//    void reporte(){
//     print("CARRERA: $name_carrera"); 
//     print("NUMERO DE CUENTA: $num_cuenta");
//     print("SEMESTRE: $semestre");
//    }
// }

```

### SCOPE DE VARIABLES, O AMBITO DE VARIABLES. 
Scope: se refiere a donde esta variable existe y tiene una relación con el lugar en el que esta fue declarada.


```python
// int x= 25; 
// void main (List<String> args) {
//   var x =5; 
//   void showNumber() {
//     var y=10; 
//     print(x); 
//     print(y); 
//   }
//   showNumber(); 
//   showX(); 
// }
```

###  Setter y Getters 
<div style= "text-align: justify"> Get: Es el metodo que ayuda a obtener y almacenar un valor de la variable dada (get "obtener")  </div>
 <div style= "text-align: justify">Set: es el metodo que ayuda a fijar el valor tomado de una variable en especifico.  </div>


```python
class User{ //Todas las clases empiezan con mayusculas para poder diferenciar con una variable
    //encapsulamiento de propiedades
    //encapsulamientO, consiste en ocultar los atributos de la clase, el simbolo "_" hace todo privado
    String? _nombre;   <<-LAS PROPIEDADES SON PRIVADAS, ES DECIR, SOLO EL PROGRAMADOR PUEDE ACCEDER A ELLAS MEDIANTE LOS SETTER Y GETTER. 
    int? _edad; // con ? se puede indicar que es de valor nulo

    //seters
    void set nombre(String nombre) => _nombre = nombre;
    void set edad(int edad) => _edad = edad;


    //getters
    String get nombre => return _nombre!;
        //para indicar que si se puede imprimir un nulo con "!" 

    int get edad{
        return _edad!; //para indicar que si se puede imprimir un nulo con "!" 
    }
```

### EJERCICIO: HACER UNA CALCULADORA CON CLASES


```python
class Calculadora {
// int a= 0; 
// int b= 0; 
// int suma(int a, int b) => a+b; 
// int resta(int a, int b) => a-b; //funcion declarativa 
// int multi(int a, int b) => a*b; //funcion declarativa 
// double divi(int a, int b) => a/b; //funcion declarativa 


void Calcular (int a, int b, String opcion) {
// Calculadora calc = Calculadora(); 
// calc.a = a; 
// calc.b = b; 
//   switch(opcion) {
//     case '+': 
//     print(calc.suma(a,b)); 
//     break; 
//     case '-': 
//     print(calc.resta(a, b));
//     break; 
//     case '*': 
//     print(calc.multi(a,b)); 
//     break; 
//     case '/':
//     print(calc.divi(a,b));
//     break; 
//     default:

//     }
//   }
// }
```

### CONSTRUCTORES 
 <div style= "text-align: justify"> Son los métodos que se crean por defecto al crear una instancia de clase, verdaderamente no es necesario hacer un constructor para que un programa dentro de Dart corra, sin embargo, son necesarios si se usan las propiedades privadas, es el uso más correcto de las propiedades privadas. El constructor, inicializa la instancia de la clase con los argumentos definidos  </div>


EL CONSTRUCTOR DEBE DE TENER OBLIGATORIAMENTE EL NOMBRE DE LA CLASE, LLEVA LOS ARGUMENTOS QUE QUIERO QUE LLEVE, Y SU PALABRA RESERVADA ES "THIS", INDICA QUE SE  INICIA EN TAL VARIABLE. 
EN EL CONSTRUCTOR, NO SE USAN LOS SETERS NI GETTERS, SIN EMBARGO ES NECESARIO HACERLOS PARA PODER MODIFICAR LOS DATOS POSTERIORMENTE. 


```python
void main (){
Vehiculo names= Vehiculo(4,"ROJO", "Cruze 906", "CHEVROLET");
// names.numllantas= 1254;
// names.color ="rojo";
// names.modelo ="CRUZE 906"; 
// names.marca ="CHEVROLET";
names.rellenar();


}

class Vehiculo {

  int? _numllantas; 
  String? _color; 
  String? _modelo; 
  String? _marca; 

  // void arrancar() {
  // print("ARRANCA");
  // }
  // void corre() {
  // print("CORRE"); 
  // }
  // void frenar() {
  // print ("FRENAR");
  // }

  void set numllantas(int numllantas){
    _numllantas = numllantas; 
  }

  void set color(String color){
    _color= color; 
  }

  void set modelo(String modelo){
    _modelo=modelo; 
  }

  void set marca(String marca){
    _marca=marca; 
  }

  int get numllantas{
    return _numllantas!; 
  }
  String get color{
    return _color!;
  }

  String get modelo{
    return _modelo!;
  }

  String get marca{
    return _marca!;
  }

  void rellenar(){
    print("NUMERO LLANTAS=> $_numllantas"); 
    print("COLOR => $_color");
    print("MARCA DEL AUTO=> $_marca");
    print("MODELO DEL AUTO => $_modelo");
  }

  //CONSTRUCTOR 

  // Vehiculo (int numllantas, String color, String marca, String modelo){
  // this._numllantas = numllantas; 
  // this._color= color; 
  // this._marca= marca; 
  // this._modelo= modelo; 
  // }

//CONSTRUCTOR FORMA CORTA
Vehiculo (this._numllantas, this._marca, this._color, this._modelo);

```

### Mixin

Un mixin es una clase cuyos métodos y propiedades pueden ser utilizados por otras clases, sin herencia.
Para poder hacer un mixin con varias subclasaes es necesario usar la palabra with. 
La palabra clave "extends" hace referencia que se hará una toma de propiedades de ésta hasta tal clase. 


```python
class Animal{ ###CLASE DE NOMBRE ANIMAL
String? _especie; 
String? _zona; 
void comer (){
  print("COME"); 
}

void set especie(String especie){
  _especie = especie; 
}

void set zona(String zona){
  _zona = zona; 
}

String get especie{
  return _especie!;
}

String get zona{
  return _zona!; 
}
}

class Ave{ ###CLASE DE NOMBRE AVE
String? _tamano; 
void volar(){
   print("VUELA"); 
}


void set tamano(String tamano) {
_tamano = tamano; 
}

String get tamano{
  return _tamano!; 
}

}


###MIXIN
class Mounstro extends Animal with Ave{ //MIXTING, ES EL MÉTODO QUE HEREDA TRAS HEREDACION, ES DECIR, CREA UNA CADENA; COMO MAMÁ, PAPÁ E HIJO 
String?  habitat; 
String? alimentacion; 
}
```
