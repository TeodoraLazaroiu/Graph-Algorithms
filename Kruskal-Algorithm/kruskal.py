# algoritmul lui kruskal pentru generarea
# arborelui partial de cost minim

# Complexitate: O(m log n)

def listaMuchii(fisier):
    
    f = open(fisier)

    m = int(f.readline().split()[1])
    lista = [[] for _ in range(m)]

    i = 0
    for linie in f:
        lista[i] = [int(x) for x in linie.split()]
        i = i + 1

    lista.sort(key = lambda x : x[2])

    f.close()

    return lista

def union(nod1, nod2, marker):

    m1 = marker[nod1 - 1]
    m2 = marker[nod2 - 1]

    for i in range (len(marker)):
        if marker[i] == m2:
            marker[i] = m1

def kruskal(lista, marker, n):

    arbore = []
    numar = 0

    for muchie in lista:

        # daca cele doua varfuri nu sunt deja unite
        # le adaugam in arborele de cost minim

        if marker[muchie[0] - 1] != marker[muchie[1] - 1]:
            
            arbore.append(muchie)

            # marcam cele doua noduri cu acelasi numar
            # pentru a arata ca sunt unite
            union(muchie[0], muchie[1], marker)

            numar = numar + 1
        
            if (numar == n - 1):
                break
    
    return arbore

# lista muchii sortate crescator in functie de cost
lista = listaMuchii("kruskal.in")

f = open("kruskal.in", "r")

n, m = [int(x) for x in f.readline().split()]

# lista prin care tin cont care
# noduri sunt unite intre ele
marker = [i for i in range(n)]

arboreCostMinim = kruskal(lista, marker, n)

print(arboreCostMinim)

f.close()