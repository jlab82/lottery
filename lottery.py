#coding: utf-8
import random
#función que recorre una lista y devuelve True si lo encuentra
def buscar_numero_en_lista(nombre_lista, num_aleatorio):
    for pos in range(len(nombre_lista)):
        if nombre_lista[pos] == num_aleatorio:
            return True


print("Bienvenidos al generador de números de lotería")
num = int(raw_input("Por favor, introduce cuántos números quieres generar: "))
lista = []
posicion = 0
while posicion < num:
    aleatorio = random.randint(1, 99)
    if not buscar_numero_en_lista(lista, aleatorio):
        lista.append(aleatorio)
    else:
        posicion -= 1
    posicion += 1
print "La cantidad de números a generar es {}" .format(num)
print lista
print "FINAL"






