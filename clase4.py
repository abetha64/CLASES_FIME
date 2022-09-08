# lista1= [1,2,3,4,5]
# print (lista1)
# lista2= [1, 3.14, "a", True, (1,2,3), {8,"a", 5.4}] ##aqui hay, listas, sets y conjuntos (en ese orden)
# print(lista2)

# print(len(lista1)) ##LEN, es una funcion que nos dice la cantidad de elementos que hay en el argumento y te lanza un unumero entero ##
# print(lista2[2])

# lista_cal = []
# lista_cal.append(5)
# print(lista_cal)
# lista_cal.append(8)
# print(lista_cal)

##RELLENAR UNA LISTA CON LOS NUMEROS NATURALES DEL 1 AL 10

# lista_num_naturales =[]
# for a in range (0,11): ##recuerda ponele al final de una delclaracion los ":"
#     lista_num_naturales.append(a) ##añade los numereos a la lista declarada anterriormente con el ciclo, llamado "a"
#     print(lista_num_naturales)

#     ##indices numeros negativos 
#     print(lista_num_naturales(-4))

# ##SLICES (REBANADAS)
# lista1= [1,2,3,4,5,6,7,8,9,10]
# print(lista1)
# print(lista1[:]) ##imprime exactamente la lista en general 
# print(lista1[0:10]) ##imprime lo mismo que la anterior 
# print(lista1[int(len(lista1)/2):]) ##imprime la mitad de los elementos de la lista

# print(lista1[int(len(lista1)/2)]) 
# print(lista1[0:-1])
# print(lista1[3:7])
# print(lista1[-7:-3])

# lista1= [1, 'dos',  3, 'cuatro']
# # print(lista1)
# lista2=lista1
# print(f"lista 1: {lista1}")
# print(f"lista 2: {lista2}")
# lista2[1]=lista1
# print("________")
# print(f"direccion: {id(lista1)}, lista 1: {lista1}") ##AQUI, LO QUE PASA ES QUE LA LISTA 1 NO SE ALMACENA EN ALGUN LADO, POR LO QUE LA DIRECCION ES EXÁCTAMENTE LA MISMA QUE LA LISTA2 Y NO HAY UNA LOCALIDAD ÚNICA
# print(f"direccion: {id(lista2)}, lista 1: {lista2}")
# print("FORMA CORRECTA")
# lista1 = [1, "dos", 3, "cuatro"]
# lista2=lista1[:]
# print(f"direccion lista1: {id(lista1)}") ##Pero aqui, existe un almacenamiento donde cada lista tiene su propio espacio, por lo que los datos de cada uno se queda intactos 
# print(f"direccion lista2: {id(lista2)}")

lista1 =[0,1,2,3,4]
lista2= [5,6,7]
#lista1[5:] =[5,6,7] ##manera uno de añadir elementos a una lista 
#lista1.append(5) #manera 2 de aladir elementos (recordar que el append añade elementos pero hasta el final)
# lista1[len(lista1):] = lista2
# print(lista1)

# lista1[:0] =lista2 ##metodo para insertar los numeros al inicio de la lista
# print(lista1)

# lista1.append(lista2)
# print(lista1)

# lista1.extend(lista2)
# print(lista1)

# ##COMO BORRAR UN ELEMENTOS EN UNA LISTA 
# # del (lista1[0])
# # print(lista1)

# ##BORRAR CON SLICES 
# del(lista1[2:5])
# print(lista1)