import csv
import random
import math
from tabulate import tabulate #tabula la información de cada uno de los atributos.


def dist_eucl(punto1, punto2):
    suma = 0
    for i in range(len(punto1)):
        suma += (punto1[i] - punto2[i]) ** 2
    return math.sqrt(suma)

def k_medias(datos, k, max_iteraciones=100):
    centroides = random.sample(datos, k)
    
    for _ in range(max_iteraciones):
        grupos = [[] for _ in range(k)]
        
        for dato in datos:
            distancias = [dist_eucl(dato, centroide) for centroide in centroides]
            indice_min_distancia = distancias.index(min(distancias))
            grupos[indice_min_distancia].append(dato)
        
        nuevos_centroides = []
        for grupo in grupos:
            nuevo_centroide = [sum(valores) / len(grupo) for valores in zip(*grupo)]
            nuevos_centroides.append(nuevo_centroide)
        
        if nuevos_centroides == centroides:
            # Convertir listas en tablas
            tabla_viejos_centroides = tabulate(centroides, headers=["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4"])
            tabla_nuevos_centroides = tabulate(nuevos_centroides, headers=["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4"])

            # Imprimir tablas donde esten los centroides acomodados segun la iteracion
            print( " \n CENTROIDES VIEJOS: " )
            print(tabla_viejos_centroides)

            print( "\n NUEVOS CENTROIDES:"  )
            print(tabla_nuevos_centroides)
            break
        # convierte de listas en tablas
        tabla_viejos_centroides = tabulate(centroides, headers=["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4"])
        tabla_nuevos_centroides = tabulate(nuevos_centroides, headers=["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4"])

        # imprime las tablas
        print( "\nCENTROIDES VIEJOS:" )
        print(tabla_viejos_centroides)

        print(  "NUEVOS CENTROICES"  )
        print(tabla_nuevos_centroides)
        centroides = nuevos_centroides
    
    return grupos, centroides

def main():
    nombre_archivo = 'Iris.csv' #puse un input para solicitar el nombre del archivo
    datos = []
    dtosID = []
    datos_prueba = []
    datos_pruebaID = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)
        for fila in lector_csv:
            datos.append([float(valor) for valor in fila[1:-1]])
            dtosID.append([float(valor) for valor in fila[1:]])
            #datos2.append([float(valor) for valor in fila [:-1]]) #ESTA LINEA ESTÁ SIENDO EDITADA
            #print(datos2)

    porcentaje = int(0.10*len(datos)) #se saca el 10% de la longitud total del archivo
    datos_prueba = datos[:porcentaje] #se extraen los primeros 15 datos del array
    datos = datos[porcentaje:] #se quitan los 15 primeros datos del array
    
    datos_pruebaID = dtosID[:porcentaje]
    dtosID = dtosID[porcentaje:]
            
    k = int(input(  "ESCRIBE EL NUMERO DE CLUSTERS A ELECCION => " ))
    grupos, centroides = k_medias(datos, k)
    
    
    tabla_centroides = tabulate(centroides, headers=["ATRIBUTO 1", "ATRIBUTO 2", "ATRIBUTO 3", "ATRIBUTO 4"]) # Mostrar resultados
    print( "\n RESULTADOS DEL ENTRENAMIENTO:"  )
    print(tabla_centroides)
    
    #muestra datos extraidos
    print("DATOS NO USADOS EN EL ENTRENAMIENTO=>>>  \n"  )
    for ver in datos_prueba:
        print(ver)
    print("\n")
    
    acertados = 0
    porcentaje_aciertos = 0
    while True:

        # SOLICITA NUEVOS
        print( "\nPOR FAVOR, INGRESA NUEVOS DATOS:"  )
        nuevos_datos = [float(input(  f"ATRIBUTO {i + 1}: "  )) for i in range(4)]
        
        # Encontrar grupo para nuevos datos
        distancias_nuevos = [dist_eucl(nuevos_datos, centroide) for centroide in centroides]
        indice_min_distancia_nuevos = distancias_nuevos.index(min(distancias_nuevos))
        print(f"\nEL NUEVO DATO PERTENECE AL GRUPO=>>   {indice_min_distancia_nuevos}")
        print(nuevos_datos)

        coincidencia = False
        for valor2 in datos_pruebaID:
            if valor2[:4] == nuevos_datos:
                print(f"El dato realmente pertenecia a =>> {valor2[4:]}")
                coincidencia = True
                porcentaje_aciertos = porcentaje_aciertos + 1
                if valor2[4:] == [indice_min_distancia_nuevos]:
                    acertados = acertados + 1
                print(f"El porcentaje en aciertos es =>> {(acertados*100)/porcentaje_aciertos}")

        if coincidencia == False:
            print("No hay coincidencia")

        cerrar = input("¿DESEA REALIZAR MAS PRUEBAS? (S/N)=>> ")
        if cerrar.upper() != 'S':
            break

if __name__ == "__main__":
    main()