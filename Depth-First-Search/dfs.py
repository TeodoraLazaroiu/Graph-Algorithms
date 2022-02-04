# parcurgerea unui graf in adancime in mod recursiv

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

lista = listaAdiacenta("dfs.in","neorientat")

# functia primeste o lista de adiacenta
# si nodul de start al parcurgerii

def dfs(lista, nod):

    if nod not in vizitat:

        vizitat.append(nod)
        g.write(f"{nod} ")

        for vecin in lista[nod - 1]:
            dfs(lista, vecin)

f = open("dfs.in", "r")
g = open("dfs.out", "w")

vizitat = []

# numarul de noduri si numarul de muchii
n, m = [int(x) for x in f.readline().split()]

for nod in range(1, len(lista) + 1):
    if nod not in vizitat:
        dfs(lista, nod)
        g.write("\n")

f.close()
g.close()