n = int(input("Podaj liczbe wierszy: "))

def pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

triangle = pascal(n)


napisy = []
for row in triangle:
    s = ""
    for liczba in row:
        s = s + str(liczba) + " "
    napisy.append(s)


ostatni_wiersz = napisy[n-1]
max_szerokosc = len(ostatni_wiersz)

for s in napisy:
    print(s.center(max_szerokosc))
