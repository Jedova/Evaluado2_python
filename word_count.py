
with open("lorem_ipsum.txt", "r", encoding="utf-8") as file:
    texto_1=file.read()

import string

##Contar caracteres##
total_con_espacios = len(texto_1)
total_sin_espacios = len(texto_1.replace(" ", ""))

##Limpiar puntuación para contar palabras reales##
texto_sin_puntuacion = texto_1.translate(str.maketrans('', '', string.punctuation))

##Dividir palabras##
palabras = texto_sin_puntuacion.lower().split()

##Contar palabras##
total_palabras = len(palabras)

##Contar palabras distintas##
palabras_distintas = set(palabras)
total_distintas = len(palabras_distintas)

##Mostrar resultados##
print(f"Total de caracteres con espacios: {total_con_espacios}")
print(f"Total de caracteres sin espacios: {total_sin_espacios}")
print(f"Total de palabras: {total_palabras}")
print(f"Número de palabras distintas: {total_distintas}")
