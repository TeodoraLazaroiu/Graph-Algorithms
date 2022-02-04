# Algoritmul lui Floyd-Warshall pentru determinarea drumului minim
# intre toate perechile de varfuri intr-un graf orientat, ponderat ce 
# nu poate contine circuite negative si poate avea ponderi negative
# De asemenea, se pot detecta circuitele negative daca exista

# Complexitate: O(n^3)

def matriceDistante(fisier, orientare):
    global n, m

    f = open(fisier, "r")

    n, m = [int(x) for x in f.readline().split()]

    lista = []
    matrice = []

    for i in range(n):
        matrice.append([0 if j == i else inf for j in range(n)])

    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        lista.append(tuple(aux))

    for muchie in lista:
        # calculam distanta pentru fiecare element al matricei
        matrice[muchie[0] - 1][muchie[1] - 1] = muchie[2]

        if orientare == "neorientat":
            matrice[muchie[1] - 1][muchie[0] - 1] = 1

    return matrice

def afisareDrum(i, j):
    if i != j:
        afisareDrum(i, p[i][j])
    
    print(j + 1, end = " ")

def floyd(d, p):
    for i in range(n):
        for j in range(n):
            if d[i][j] == inf:
                p[i][j] = 0
            else:
                p[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]

inf =  float('inf')
d = matriceDistante("floyd.in", "orientat")

# matrice de predecesori
p = [[0] * n for i in range(n)]

# calculeaza matricea de distante
# si matricea de predecesori
floyd(d,p)

# exemplu de afisare: drumul minim de la 2 la 1
afisareDrum(2,1)