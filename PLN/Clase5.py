import re

carpeta="Documentos\\"

with open (carpeta + "archivo_nuevo.txt", "r" ) as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"(el|los) PLN?") ##Imprime palabra con el o los dependiendo la frase
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))