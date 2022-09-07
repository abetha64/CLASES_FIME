
# n1= 10 
# msg= "hola"

# print (n1, msg)
# print (str, (n1)+ msg)
# #fstring 
# print(f"{n1} {msg}")

#hacer una funcion que reciba el nombre de una persona 
#el año de nacimiento y el año actual retornando 
# el mensaje "hola, <nombre>, tienes <edad> años "

# def nombre_edad (nombre: str, año_nac: int, año_actual: int)-> str: 
#     edad=año_actual - año_nac

#     return f"hola {nombre},  tienes {edad} años" #PRIMERA FORMA DE HACERLO

# def nombre_edad2 (nombre: str, año_nac: int, año_actual: int)-> str: #SEGUNDA FORMA DE HACERLO
#     return f"hola {nombre},  tienes {año_actual- año_nac} años"

# def nombre_edad3 (nombre: str, año_nac: int, año_actual: int)-> str: #FORMA TRES DE HACERLO
#     return f"Hola {nombre}, tienes {calcular_edad(año_nac-año_actual)} años"


# print (nombre_edad("Alba", 2002, 2022))
# print (nombre_edad2("Alba", 2002, 2022))

#LISTAS
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"] #LISTAS

# print(f"Alumnos:  {alumnos}")

# for i in range (len (alumnos)): 
#     print (f"Alumnos: {alumnos[i]}")

# #TUPLAS 
# for i in range (len (alumnos)): 
#     print (f"Alumnos: { i + 1}: {alumnos[i]}")

# #SETS 
# alumnos = {"Hugo", "Paco", "Luis", "Lupita"}
# print (f"Alumnos: {alumnos}")

# #DICCIONARIOS 
# alumnos={"Nombre": "Hugo", "materia1": 10, "Materia2": 5 }
# print(f"Alumnos: {alumnos}")
# print(f"Alumno: {alumnos ['nombre']}")


#LISTAS A SETS 
# numeros_list = (1,2.3,1,1,2,2,2,3,3,4,5,7,8,8,9,9)
# numeros_sets = {1,2.3,1,1,2,2,2,3,3,4,5,7,8,8,9,9}

# print(numeros_list)
# print (numeros_sets)

#simulacion de base de datos 

# e = ["NOMBRE", "EST DAT", "PROG FUNC", "INGLES"]
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
# m_e_d= (9,8,7,6)
# m_e_p= (9,5,9,8)
# m_e_f= (9,8,7,6)
# m_e_ñ= (9,8,7,6)

# print (f"{e[0]:^10}{e[1]:^10}{e[2]:^10}{e[3]:^10}")
# for i in range (len(alumnos)): 
#     print (f"{alumnos [i]:^10}{m_e_d[i]:^10} {m_e_p[i]:^10} {m_e_f[i]:^10} {m_e_ñ[i]:^10}")



