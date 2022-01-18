# algoritmul de parcurgere in latime a unui graf

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

lista = listaAdiacenta ("bfs.in", "neorientat")

# functia primeste o lista de adiacenta
# si nodul de start al parcurgerii

def bfs(lista, nod):

    vizitat.append(nod)
    coada.append(nod)

    # in coada vor fi introduse nodurile pe masura ce sunt parcurse si vor
    # fi eliminate cand sunt parcursi toti vecinii nodului respectiv
    while coada:
        s = coada.pop(0)
        g.write(f"{s} ")
        # cand un nod este eliminat din coada este si afisat

        # parcurge toti vecinii nodului curent
        # si ii marcheaza in vectorul de vizitati
        for vecin in lista[s - 1]:
            if vecin not in vizitat:
                vizitat.append(vecin)
                coada.append(vecin)

f = open("bfs.in", "r")
g = open("bfs.out", "w")

coada = []
vizitat = []

# numarul de noduri, muchii si nodul de start
n, m, x = [int(x) for x in f.readline().split()]

bfs(lista, x)

f.close()
g.close()