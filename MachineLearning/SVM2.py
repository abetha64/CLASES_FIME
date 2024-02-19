#PROGRAMA DE MAQUINA DE SOPORTE VECTORIAL

#import numpy as np
import pandas as pd
from math import dist
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def Eliminar_columnas(datos, columnas):
    while True:
        nombre = input('Ingrese el nombre de la columna a eliminar: ')
        if nombre in columnas:
            datos = datos.drop([nombre], axis=1)
            return datos
        else:
            print('\nIngrese un nombre de columna válido, recuerda respetar las mayúsculas.\n')

def AgregarClasePivotes(x_train:list, y_train:list, pivote:list):
    pos_piv = x_train.index(pivote)
    clase_piv = y_train[pos_piv]
    if clase_piv == 0:
        pivote.append(1)
    else:
        pivote.append(-1)

def Grafica(x, modelo, tipo):
    mensaje = f'SVM Resultados de los {tipo} ' 
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(x.drop(['Originales', 'Nuevos'], axis=1))
    plt.scatter(x_pca[:, 0], x_pca[:, 1], c=modelo, cmap='rainbow')
    plt.title(mensaje)
    plt.show()

if __name__ == "__main__":
    fin = True
    while fin:
        
        datos = pd.read_csv('Iris.csv') #lee el csv

        if datos is not None:
            datos_sin_modificar = datos.copy()
            columnas = datos.columns

            while True:
                nombre = input('Ingrese el nombre de la columna con la clasificación => ')
                if nombre in columnas:
                    break
                else:
                    print('\nIngrese un nombre de columna válido, recuerda respetar las mayúsculas.\n')

            clases = datos[nombre]
            print("\n\nDatos ingresados: \n", datos_sin_modificar)

        # Limpieza de datos
        datos = Eliminar_columnas(datos, columnas)
        des = 's'
        while(des != 'n'):
            try: 
                des = input("¿Desea eliminar otra columna? y/n ")
                des = des.lower()
                if des == 'y':
                    datos =Eliminar_columnas(datos, columnas) 
                else:
                    if des != 'n':
                        print("\nIngrese un valor valido.\n")
            except:
                print("\nIngrese un valor valido.\n")

        #? Extraccion y division de datos de entrenamiento y prueba
        x_train, x_test, y_train, y_test = train_test_split(datos, clases, test_size=0.2, random_state=0)
        x_train = (x_train.to_numpy()).tolist()
        y_train = (y_train.to_numpy()).tolist()
        x_test_list = x_test.copy()
        x_test_list = (x_test_list.to_numpy()).tolist()
        y_test = (y_test.to_numpy()).tolist()

       

    # Divide los datos de entrenamiento por clase
        cero = []
        uno = []
        for i in range(len(x_train)):
            if y_train[i] == 0:
                cero.append(x_train[i])
            else:
                uno.append(x_train[i])
        # print(cero, '\n\n\n', uno)

#! Aplicacion del algoritmo
    #? Eleccion de vectores auxiliares
        distancias = []
        posiciones = []
        for c in cero:
            for i in range(len(uno)):
                distancias.append(dist(c, uno[i]))
                posiciones.append([c, uno[i]])
        # print(distancias)
        minimo = (min(distancias))

        #* Distancia y posicion de los pivotes 1 y 2
        posi = distancias.index(minimo)
        pnt_min = posiciones[posi] 

        # print(minimo, pnt_min)

        #* Encontramos entre los pivotes 1 y 2 el siguiente valor mas pequeno
        pos_pivote3 = []
        dis_pivote3 = []
        for i in range(len(posiciones)):

            if i!=posi:
                pos_pivote3.append(i)
       
        for i in pos_pivote3:
            dis_pivote3.append(distancias[i])
        # print(dis_pivote3)
        min_piv3 = (min(dis_pivote3)) # Distancia menor entre las posiciones encontradas
        # print(min_piv3) #bandera
        pos_min_piv3 = distancias.index(min_piv3)
        if(pos_min_piv3 >= posi): pos_min_piv3 + 1
        posicion_piv3 = posiciones[pos_min_piv3] #* Pivote 3
        # print(min_piv3, posicion_piv3)


        # Asignacion de pivotes
        pivote1 = pnt_min[0]
        pivote2 = pnt_min[1]

        if posicion_piv3 [0] != pivote1 and posicion_piv3[0] != pivote2:
            pivote3 = posicion_piv3[0]
        else:
            pivote3 = posicion_piv3[1]

        pivote1.append(1)
        pivote2.append(1)
        pivote3.append(1)

        AgregarClasePivotes(x_train, y_train, pivote1)
        AgregarClasePivotes(x_train, y_train, pivote2)
        AgregarClasePivotes(x_train, y_train, pivote3)

        print(f'\nPivotes:\n{pivote1[0:1]}\n{pivote2[0:1]}\n{pivote3[0:1]}')

    # Calculos de valores alfa
        #* Multiplicaciones
        m11 = (pivote1[0] * pivote1[0]) + (pivote1[1] * pivote1[1]) + 1
        m12 = (pivote1[0] * pivote2[0]) + (pivote1[1] * pivote2[1]) + 1
        m13 = (pivote1[0] * pivote3[0]) + (pivote1[1] * pivote3[1]) + 1
        m21 = (pivote2[0] * pivote1[0]) + (pivote2[1] * pivote1[1]) + 1
        m22 = (pivote2[0] * pivote2[0]) + (pivote2[1] * pivote2[1]) + 1
        m23 = (pivote2[0] * pivote3[0]) + (pivote2[1] * pivote3[1]) + 1
        m31 = (pivote3[0] * pivote1[0]) + (pivote3[1] * pivote1[1]) + 1
        m32 = (pivote3[0] * pivote2[0]) + (pivote3[1] * pivote2[1]) + 1
        m33 = (pivote3[0] * pivote3[0]) + (pivote3[1] * pivote3[1]) + 1
        
        incremento = ((m11 * m22 * m33) + (m21 * m32 * m13) + (m31 * m12 * m23)) - ((m13 * m22 * m31) + (m23 * m32 * m11) + (m33 * m12 * m21))

        m11c = pivote1[3]
        m21c = pivote2[3]
        m31c = pivote3[3]

        incremento1 = ((m11c * m22 * m33) + (m21c * m32 * m13) + (m31c * m12 * m23)) - ((m13 * m22 * m31c) + (m23 * m32 * m11c) + (m33 * m12 * m21c))

        m12c = pivote1[3]
        m22c = pivote2[3]
        m32c = pivote3[3]

        incremento2 = ((m11 * m22c * m33) + (m21 * m32c * m13) + (m31 * m12c * m23)) - ((m13 * m22c * m31) + (m23 * m32c * m11) + (m33 * m12c * m21))

        m13c = pivote1[3]
        m23c = pivote2[3]
        m33c = pivote3[3]

        incremento3 = ((m11 * m22 * m33c) + (m21 * m32 * m13c) + (m31 * m12 * m23c)) - ((m13c * m22 * m31) + (m23c * m32 * m11) + (m33c * m12 * m21))

        #* Valores de alfa
        alfa1 = incremento1 / incremento
        alfa2 = incremento2 / incremento
        alfa3 = incremento3 / incremento
        print('\nValores de alfa:\n',alfa1, alfa2, alfa3, '\n')

    #? Resultado de la linea
        #* Parametros
        wx = (alfa1 * pivote1[0]) + (alfa2 * pivote2[0]) + (alfa3 * pivote3[0])
        wy = (alfa1 * pivote1[1]) + (alfa2 * pivote2[1]) + (alfa3 * pivote3[1])
        wb = alfa1 + alfa2 + alfa3
        
    #? Predicciones
        nuevas_clases = []
        for punto in x_test_list:
            prediccion = (wy * punto[1]) + (wx * punto[0]) + wb
            
            if prediccion < 0:
                # -1 -> 1 +1 -> 0
                nuevas_clases.append(1)
            else:
                nuevas_clases.append(0)

        # Impresion de resultados
        x_test['Originales'] = y_test
        x_test['Nuevos'] = nuevas_clases

        print(f"\n\n\nResultados:\n{x_test}")
        coincidencias = (x_test['Originales'] == x_test['Nuevos']).sum()
        total_elementos = len(x_test)
        porcentaje_coincidencia = (coincidencias / total_elementos) * 100

        print(f"Porcentaje de coincidencia: {porcentaje_coincidencia:.2f}%")

        Grafica(x_test, nuevas_clases, 'datos prueba')

        des = 's'
        while(des != 'y'):
            try: 
                des = input("¿Desea volver a usar el progama? y/n ")
                des = des.lower()
                if des == 'n':
                    fin = False
                    des = 'y'
                else:
                    if des != 'y':
                        print("\nIngrese un valor valido.\n")
            except:
                print("\nIngrese un valor valido.\n")

            
