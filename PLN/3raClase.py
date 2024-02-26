
# #ejercicios de archivos de texto

# semana_lab= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
# print("Semana laboral: ", semana_lab)

# # print("Día1= ", semana_lab[0])
# # print("Día2= ", semana_lab[1])
# # print("Día3= ", semana_lab[2])
# # print("Día4= ", semana_lab[3])
# # print("Día5= ", semana_lab[4])

# # semana_lab[4]="Sabado"
# # print(semana_lab)

# #SACAMOS LONGITUD
# # long_list=len(semana_lab)
# # print(long_list)

# #agregamos con append
# # semana_lab.append("Sábado")
# # print("La nueva lista es: ", semana_lab)

# # #pocision
# # # posicion=semana_lab.index("Míercoles")
# # # print("Posicion de Míercoles ", posicion)

# # #borra elemento de la lista 
# # del semana_lab[4]
# # print("Semana laboral: ", semana_lab)


with open("Clase3.txt", "r") as archivo:
    lineas_lista=archivo.readlines()
print(lineas_lista)

num_linea=1
line_vacia=0

for linea in lineas_lista: 
    if linea.strip() == "":
        print("La linea está vacía==> ") #cuando encuentre una linea que NO contenga texto indique que esa linea esté vacía
        line_vacia=line_vacia+1
        continue
    else:
        print ("Numero de linea: ", num_linea, ": ", linea)
    num_linea=num_linea+1
        
print("El total de lineas es: ", len(lineas_lista)) #que cuente las lineas que contiene el archivo y lo indique
print("El total de lineas vacias es: ", line_vacia) #Muestr cuantas lineas tienen texto y cuántas no 


    
