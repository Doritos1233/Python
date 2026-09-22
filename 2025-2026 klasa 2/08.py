<<<<<<< HEAD
lista = [1,69,82,7,13,21,10,54,52,25,100000]


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
    
def anomalie(lista):
    mediana = med_liczba(lista)
    anomalie = []
    
    for x in lista:
        if x > 2 * mediana or x < 0.5 * mediana:
            anomalie.append(x)
            
    return anomalie


print(f"mediana: {med_liczba(lista)}")
print(f"avg: {avg_liczba(lista)}")
=======
lista = [1,69,82,7,13,21,10,54,52,25]


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
    
def anomalie(lista):
    mediana = med_liczba(lista)
    anomalie = []
    
    for x in lista:
        if x > 2 * mediana or x < 0.5 * mediana:
            anomalie.append(x)
            
    return anomalie


print(f"mediana: {med_liczba(lista)}")
print(f"avg: {avg_liczba(lista)}")
>>>>>>> 1dd45523b45d5652d47db15093e62f50f2550991
print(f"anomalie: {anomalie(lista)}")