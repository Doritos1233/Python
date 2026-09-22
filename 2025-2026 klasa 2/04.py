
def silnia(n):
    return n * (n - 1)

print( silnia(2))

def silnia_petla(n):
    wynik = 1
    for i in range (n + 1):
        wynik *= i
    return wynik

print (silnia_petla(1))