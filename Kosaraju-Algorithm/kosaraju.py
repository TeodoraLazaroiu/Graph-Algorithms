# algoritm pentru detectarea componentelor tare conexe

def listaAdiacenta(fisier, orientare):
    
    f = open(fisier)

    n = int(f.readline().split()[0])
    lista = [[] for _ in range(n)]

    if orientare == "neorientat" or orientare == "orientat":
        for linie in f:
            i, j = [int(x) for x in linie.split()]

            if j not in lista[i -1]:
                lista[i - 1].append(j)

            if orientare == "neorientat" and i not in lista[j - 1]:
                lista[j - 1].append(i)
    else:
        exit("Orientarea grafului este gresita")

    for i in range(n):
        lista[i].sort()

    f.close()

    return lista

def reverseListaAdiacenta(fisier, orientare):
    
    f = open(fisier)

    n = int(f.readline().split()[0])
    lista = [[] for _ in range(n)]

    if orientare == "neorientat" or orientare == "orientat":
        for linie in f:
            j, i = [int(x) for x in linie.split()]

            if j not in lista[i -1]:
                lista[i - 1].append(j)

            if orientare == "neorientat" and i not in lista[j - 1]:
                lista[j - 1].append(i)
    else:
        exit("Orientarea grafului este gresita")

    for i in range(n):
        lista[i].sort()

    f.close()

    return lista

def dfs(lista, nod, componenta):
    
    if nod not in vizitat:

        vizitat.append(nod)
        componenta.append(nod)

        for vecin in lista[nod - 1]:
            dfs(lista, vecin, componenta)

        coada.insert(0, nod)

def kosaraju(lista):
    global vizitat

    for nod in range(1, len(lista) + 1):
        if nod not in vizitat:
            dfs(lista, nod, [])

    vizitat = []
    ordine = coada
    lista = reverseListaAdiacenta("kosaraju.in","orientat")

    for nod in ordine:
        if nod not in vizitat:
            componenta = []
            dfs(lista, nod, componenta)
            g.write(f"{componenta}")
            g.write("\n")

lista = listaAdiacenta("kosaraju.in","orientat")

f = open("kosaraju.in", "r")
g = open("kosaraju.out", "w")

vizitat = []
coada = []

# numarul de noduri si numarul de muchii
n, m = [int(x) for x in f.readline().split()]

kosaraju(lista)

f.close()
g.close()
