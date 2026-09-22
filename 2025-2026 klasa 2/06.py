<<<<<<< HEAD
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        zamiana = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        if zamiana:
            break
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(1 + i, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista_liczb = [random.randint(10, 100000) for _ in range(100)]

lista = [4, 67, 2, 6, 5, 67, 53]

def count_sort(lista):
    max_val = max(lista)
    count = [0] * (max_val + 1)

    for num in lista:
        count[num] += 1

    i = 0
    for num in range(len(count)):
        for x in range(count[num]):
            lista[i] = num
            i += 1
=======
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        zamiana = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        if zamiana:
            break
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(1 + i, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista_liczb = [random.randint(10, 100000) for _ in range(100)]

lista = [4, 67, 2, 6, 5, 67, 53]

def count_sort(lista):
    max_val = max(lista)
    count = [0] * (max_val + 1)

    for num in lista:
        count[num] += 1

    i = 0
    for num in range(len(count)):
        for x in range(count[num]):
            lista[i] = num
            i += 1
>>>>>>> 1dd45523b45d5652d47db15093e62f50f2550991
    return lista