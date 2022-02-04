# Algoritmul lui Dijkstra pentru determinarea drumului minim
# de la o sursa unica intr-un graf orientat, ponderat ce 
# poate contine circuite si poate avea doar ponderi pozitive

from heapq import heappush, heapify, heappop

def listaAdiacenta(fisier, orientare):

    global n, m
    
    f = open(fisier)

    n, m = [int(x) for x in f.readline().split()]
    lista = [[] for _ in range(n)]

    if orientare == "neorientat" or orientare == "orientat":
        for linie in f:
            i, j, w = [int(x) for x in linie.split()]

            if j not in lista[i -1]:
                lista[i - 1].append((j, w))

            if orientare == "neorientat" and i not in lista[j - 1]:
                lista[j - 1].append((i, w))
    else:
        exit("Orientarea grafului este gresita")

    for i in range(n):
        lista[i].sort()

    f.close()

    return lista

def dijkstra(lista):
    arbore = []
    costTotal = 0
    heap = []
    heapify(heap)
    heappush(heap, (0, 0, start))
    for i in range(1, n):
        heappush(heap, (inf, 0, i + 1)) # cost, parinte, nod
    while heap:
        tuplu = heappop(heap)
        nod = tuplu[2]
        if vizitat[nod - 1] == 0:
            vizitat[nod - 1] = 1
            costTotal += tuplu[0]
            arbore.append((tuplu[1], tuplu[2], tuplu[0]))
            for vecin in lista[nod - 1]:
                if vizitat[vecin[0] - 1] == 0 and vecin[1] + d[nod - 1] < d[vecin[0] - 1]:
                    d[vecin[0] - 1] = vecin[1] + d[nod - 1]
                    tata[vecin[0] - 1] = nod
                    heappush(heap, (d[vecin[0] - 1], nod, vecin[0]))
    arbore.pop(0)

    return d

inf = float('inf')
lista = listaAdiacenta("dijkstra.in", "orientat")

# nodul de start
start = 1
vizitat = [0 for i in range(n)]
d = [inf for i in range(n)]
tata = [0 for i in range(n)]
d[start - 1] = 0

# distanta minima de la nodul de start la fiecare nod
d = dijkstra(lista)
print(d)