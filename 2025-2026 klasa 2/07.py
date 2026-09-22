<<<<<<< HEAD
# min
# max
# avg = suma/liczba 
# geo = pierwiastek
# med = posortowac [2, 4, 5, 5, 6, 6, 8] srodkowy element listy = 5 a dla parzystej listy sa 2 elementy

lista = [5, 8, 6, 5, 4, 2, 6]

def min_liczba(lista):
    min_i = lista[0]
    for i in lista:
        if i < min_i:
            min_i = i
    return min_i

def max_liczba(lista):
    max_i = lista[0]
    for i in lista:
        if i > max_i:
            max_i = i
    return max_i

def avg_liczba(lista):
    suma = 0
    licznik = 0

    for i in lista:
        suma += i 
        licznik += 1      
    if licznik > 0:
        avg = suma / licznik
    else:
        avg = 0
    return avg
    
def geo_liczba(lista):
    a = "sigma"
    return a

def med_liczba(lista):
    n = len(lista)
    for i in range(n):
        zamiana = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        if zamiana:
            break
    if n % 2 == 1:
        return lista[n // 2]
    else:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2

print(f"liczba min: {min_liczba(lista)}")
print(f"liczba max: {max_liczba(lista)}")
print(f"liczba avg: {avg_liczba(lista)}")
print(f"liczba geo: {geo_liczba(lista)}")
print(f"liczba med: {med_liczba(lista)}")
=======
# min
# max
# avg = suma/liczba 
# geo = pierwiastek
# med = posortowac [2, 4, 5, 5, 6, 6, 8] srodkowy element listy = 5 a dla parzystej listy sa 2 elementy

lista = [5, 8, 6, 5, 4, 2, 6]

def min_liczba(lista):
    min_i = lista[0]
    for i in lista:
        if i < min_i:
            min_i = i
    return min_i

def max_liczba(lista):
    max_i = lista[0]
    for i in lista:
        if i > max_i:
            max_i = i
    return max_i

def avg_liczba(lista):
    suma = 0
    licznik = 0

    for i in lista:
        suma += i 
        licznik += 1      
    if licznik > 0:
        avg = suma / licznik
    else:
        avg = 0
    return avg
    
def geo_liczba(lista):
    a = "sigma"
    return a

def med_liczba(lista):
    n = len(lista)
    for i in range(n):
        zamiana = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        if zamiana:
            break
    if n % 2 == 1:
        return lista[n // 2]
    else:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2

print(f"liczba min: {min_liczba(lista)}")
print(f"liczba max: {max_liczba(lista)}")
print(f"liczba avg: {avg_liczba(lista)}")
print(f"liczba geo: {geo_liczba(lista)}")
print(f"liczba med: {med_liczba(lista)}")
>>>>>>> 1dd45523b45d5652d47db15093e62f50f2550991
