# Algoritmul lui Prim pentru determinarea arborelui
# partial de cost dintr-un graf conex fara cicluri

# Complexitate O(m log n)

from collections import defaultdict
import heapq

def dictionarMuchii(fisier):
    
    f = open(fisier)

    d = {}

    linie = f.readline()

    i = 0
    for linie in f:
        node1, node2, weight = [int(x) for x in linie.split()]

        if node1 not in d:
            d[node1] = {}
        if node1 in d:
            d[node1][node2] = weight

        if node2 not in d:
            d[node2] = {}
        if node2 in d:
            d[node2][node1] = weight

    f.close()

    return d

def prim (graf):
    # nodul din care se incepe cautarea
    start = 1
    arbore = defaultdict(set)

    # vectorul nodurilor vizitate
    vizitat = set([start])

    # ia muchiile care incep din A
    muchii = [(cost, start, nod) for nod, cost in graf[start].items()]

    # ordonare folosind heap
    heapq.heapify(muchii)

    costTotal = 0
    while muchii:
            # extrage cate un tuplu
            cost, nod1, nod2 = heapq.heappop(muchii)
            
            # daca al doilea nod nu a fost vizitat
            if nod2 not in vizitat:
                costTotal = costTotal + cost
                vizitat.add(nod2)
                arbore[nod1].add(nod2)

                # adauga urmatoarele muchii in heap
                for v, cost in graf[nod2].items():
                    if v not in vizitat:
                        heapq.heappush(muchii, (cost, nod2, v))

    arbore = dict(arbore)

    return arbore, costTotal

# graful contine valori de tipul node1 : {node2: weight}
graf = dictionarMuchii("prim.in")

arbore, costTotal = prim(graf)

print("Arborele este: ")
for key in arbore.keys():
    for item in arbore[key]:
        print(key, item)

print("Costul este: ", costTotal)