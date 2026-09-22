def rysuj_kwadrat():
    n = int(input("Podaj bok kwadratu: "))
    for i in range(n):
        print("*" * n*2)


def rysuj_trojkat():
    n = int(input("Podaj wysokość trójkąta: "))
    for i in range(1, n + 1):
        print("*" * i)


def rysuj_prostokat():
    a = int(input("Podaj szerokość prostokąta: "))
    b = int(input("Podaj wysokość prostokąta: "))
    for i in range(b):
        print("*" * a)

print(f"twoj kwadrat {rysuj_kwadrat()}")
print(f"twoj trojkat {rysuj_trojkat()}")
print(f"twoj prostokat {rysuj_prostokat()}")