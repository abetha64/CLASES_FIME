import re
"""
carpeta="Documentos\\"

with open (carpeta + "archivo_nuevo.txt", "r" ) as archivo:
    texto=archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," " + simbolo + " ")

palabras_lita= texto.split()
palabras_lita.sort()
for palabra in palabras_lita:
    print(palabra)

"""

carpeta="Documentos\\"

with open (carpeta + "archivo_nuevo.txt", "r" ) as archivo:
    texto=archivo.read()

expresion_reg= re.compile(r"^ESTO")
res_bus= expresion_reg.finditer(texto)
for yo in res_bus:
    print(yo.group(0))


