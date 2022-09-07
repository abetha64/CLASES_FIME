def sumar(a: int, b: int)-> int:
    return a+b

if __name__ == "__main__": 
    print (sumar(5,6))

    import sumar as s 
    import restar as a
    import multiplicar as b
    import dividir as c
    import cuadrado as d
    ##se importa y crea una librería para poder crar un modulo, la facilidad de esto es poder utilizar la libreria en varios dispositivos 
    if __name__ == "__main__": 
        print (s.sumar(5,6))
        print (a.restar(10,6))
        print (b.multiplicar(5,6))
        print (c.dividir (12,6))
        print (d.cuadrado (5))

    from operaciones import *

    if __name__ == "__main__":
        print(sumar (5,6))
        print (restar(10,6))
        print (dividir (12,6))
        print (multiplicar (5,6))
        print (cuadrado (5))

    import OPS.operaciones as OP
    import OPS.sumar as s
    import OPS.operaciones 
    import OPS.multiplicar

if __name__ == "__main__": 
    print (OP.cuadrado(5))
    print (s.sumar(3,4))
    print (multiplicar (4,5))
        
