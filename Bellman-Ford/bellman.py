# Algoritmul lui BellmanFord pentru determinarea drumului minim
# de la o sursa unica intr-un graf orientat, ponderat ce 
# nu poate contine circuite negative si poate avea ponderi negative
# De asemenea, se pot detecta circuitele negative daca exista

from heapq import heappush, heapify, heappop

def listaAdiacenta(fisier, orientare):

    global n, m, muchii
    
    f = open(fisier)

    n, m = [int(x) for x in f.readline().split()]
    lista = [[] for _ in range(n)]

    if orientare == "neorientat" or orientare == "orientat":
        for linie in f:
            i, j, w = [int(x) for x in linie.split()]

            if j not in lista[i -1]:
                lista[i - 1].append((j, w))

            muchii.append((i, j, w))

            if orientare == "neorientat" and i not in lista[j - 1]:
                lista[j - 1].append((i, w))
    else:
        exit("Orientarea grafului este gresita")

    for i in range(n):
        lista[i].sort()

    f.close()

    return lista

def bellman(lista, muchii):

    global cicluNegativ

    for i in range(1, n):
        for muchie in muchii:
            # relaxarea muchiei curente
            if d[muchie[0] - 1] + muchie[2] < d[muchie[1] - 1]:
                d[muchie[1] - 1] = d[muchie[0] - 1] + muchie[2]
                tata[muchie[1] - 1] = muchie[0]

    # detectare circuit negativ
    for muchie in muchii:
        if d[muchie[0] - 1] + muchie[2] < d[muchie[1] - 1]:
            d[muchie[1] - 1] = d[muchie[0] - 1] + muchie[2]
            tata[muchie[1] - 1] = muchie[0]
            cicluNegativ = True
            return cicluNegativ

    return d                       

inf = float('inf')
muchii = []
lista = listaAdiacenta("bellman.in", "orientat")

# nodul de start
start = 1
vizitat = [0 for i in range(n)]
d = [inf for i in range(n)]
tata = [0 for i in range(n)]
d[start - 1] = 0
cicluNegativ = False

# distanta minima de la nodul de start la fiecare nod
d = bellman(lista, muchii)

if d == True:
    print("Am detectat un ciclu negativ")
else:
    print(d)