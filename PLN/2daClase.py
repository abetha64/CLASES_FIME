abrir= "archivorandom.txt" #archivo existente
s= "archivo_nuevo.txt" #archivonuevo

e2=open(abrir, "r") #e2 es variable nueva que abre lo que contiene "abrir" con el paramentro de read jiji
s2=open( s,"w") #s2 abre el archivo nuevo y escribe

t=e2.read() #t meramente lee lo que se abrió y leyó en e2
s2.write(t)#se escribe en s2 (archivo vac+ío) lo que hay en t, que es lo del archivo "abrir"
e2.close()#cerrar
s2.close()

s3=open(s,"r")#imprime
#print(s3.read())


with open (s, "r") as archivo: 
    texto=archivo.read()
print(texto)

palabra=input("Escribe la palabra a buscar: ")

if palabra in texto:
    print(f"Palabra {palabra} encontrada")
else: 
    print(f"Palabra {palabra} no encontrada. VERIFIQUE")

