import pandas as pd
import numpy as np
from prettytable import PrettyTable
from colorama import Fore, init, Style
init()

# Lectura del archivo CSV
Datos = pd.read_csv('Iris.csv')

# Obtención de las columnas disponibles para la selección
columnas_csv = Datos.drop(['Species'], axis=1).columns
column_dict = {str(i): col for i, col in enumerate(columnas_csv)}

print(Fore.MAGENTA + "\nLista de variables disponibles en el archivo:" + Style.RESET_ALL)
for j, columnaa in enumerate(columnas_csv):
    print(f"{j}.- {columnaa}")

# Solicitar al usuario la selección de la variable dependiente
opcion = input(Fore.YELLOW + "Ingrese el número de la columna que desea como variable dependiente: " + Style.RESET_ALL)

if opcion in column_dict:
    # Obtención de la variable dependiente seleccionada por el usuario
    Dependiente = column_dict[opcion]
    List_independiente = np.array(Datos.drop(['Species', Dependiente], axis=1))
    List_dependiente = np.array(Datos[Dependiente])
else:
    print("Opción no válida")

def matriz_vector(inde, depe):
    """
    Calcula la matriz y el vector necesarios para el cálculo de la regresión lineal.

    Args:
    inde (numpy.ndarray): Matriz de variables independientes.
    depe (numpy.ndarray): Vector de variable dependiente.

    Returns:
    Tuple[numpy.ndarray, numpy.ndarray, int, int]: Matriz, vector, número de variables independientes y número de observaciones.
    """
    K = inde.shape[1]
    N = len(inde)
    Mat = np.zeros((K + 1, K + 1))
    Vec = np.zeros(K + 1)

    # Cálculo de la matriz y el vector
    Mat[0, 0] = N
    for i in range(1, K + 1):
        Mat[0, i] = Mat[i, 0] = np.sum(inde[:, i - 1])
        for j in range(1, K + 1):
            Mat[i, j] = np.sum(inde[:, i - 1] * inde[:, j - 1])
            
    Vec[0] = np.sum(depe)
    for i in range(1, K + 1):
        Vec[i] = np.sum(inde[:, i - 1] * depe)

    return Mat, Vec, K, N

# Función para resolver la matriz mediante el método de eliminación Gaussiana
def resolu_mat(mat, vec):
    """
    Resuelve la matriz usando el método de eliminación Gaussiana.

    Args:
    mat (numpy.ndarray): Matriz.
    vec (numpy.ndarray): Vector.

    Returns:
    numpy.ndarray: Solución de la matriz.
    """
    SOLU = np.linalg.solve(mat, vec)
    return SOLU

# Función para calcular el Error Estándar de Estimación Múltiple
def eeem(inde, depe, solu, k, n):
    """
    Calcula el Error Estándar de Estimación Múltiple.

    Args:
    inde (numpy.ndarray): Matriz de variables independientes.
    depe (numpy.ndarray): Vector de variable dependiente.
    solu (numpy.ndarray): Solución de la matriz.
    k (int): Número de variables independientes.
    n (int): Número de observaciones.

    Returns:
    Tuple[float, numpy.ndarray, numpy.ndarray, numpy.ndarray]: Error Estándar de Estimación Múltiple, Error Cuadrático, Predicción, Error.
    """
    PREDI = np.dot(inde, solu[1:]) + solu[0]
    ERROR = abs(depe - PREDI)
    SCE = np.square(ERROR)
    EEEM = np.sqrt(np.sum(SCE)/(n - (k + 1)))
    return EEEM, SCE, PREDI, ERROR

# Función para calcular el Coeficiente de Determinación Múltiple
def cdm(depe, sce, predi):
    """
    Calcula el Coeficiente de Determinación Múltiple.

    Args:
    depe (numpy.ndarray): Vector de variable dependiente.
    sce (numpy.ndarray): Error Cuadrático.
    predi (numpy.ndarray): Predicción.

    Returns:
    Tuple[float, numpy.ndarray]: Coeficiente de Determinación Múltiple, Error Residual Cuadrático.
    """
    SCR = np.square(np.mean(depe) - predi)
    CDM = np.sum(SCR) / (np.sum(SCR) + np.sum(sce))
    return CDM, SCR

# Cálculo de la matriz y vector para la regresión lineal
Mat, Vec, K, N = matriz_vector(List_independiente, List_dependiente)
Solu = resolu_mat(Mat, Vec)

# Cálculo del Error Estándar de Estimación Múltiple
EEEM, SCE, PREDI, ERROR = eeem(List_independiente, List_dependiente, Solu, K, N)

# Cálculo del Coeficiente de Determinación Múltiple
CDM, SCR= cdm(List_dependiente, SCE, PREDI)

if __name__=="__main__":
    # Creación de una tabla para mostrar los resultados
    tabla = PrettyTable()

    tabla.add_column("Y", List_dependiente)
    columnas = [col for col in Datos.columns if col != 'Species' and col != Dependiente]

    # Agregar columnas a la tabla
    for i in range(len(columnas)):
        tabla.add_column(f"{columnas[i]}", List_independiente[:, i])
    tabla.add_column("Predicción", PREDI)
    tabla.add_column("Error", ERROR)
    print(tabla)

    # Mostrar los resultados
    print(Fore.RED +"\n\nError estandar de determinación múltiple:"+ Style.RESET_ALL, [EEEM])
    print(Fore.GREEN +"\nCoeficiente de determinación múltiple:"+ Style.RESET_ALL, [CDM])
    print(Fore.YELLOW +"\nSolución de la ecuación:", " + ".join([f"{Solu[i]}x{i}" if i > 0 else f"{Solu[i]}" for i in range(len(Solu))])+ Style.RESET_ALL)