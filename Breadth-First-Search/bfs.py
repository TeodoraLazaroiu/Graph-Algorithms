# algoritmul de parcurgere in latime a unui graf

import listaAdiacenta

lista = listaAdiacenta.listaAdiacenta ("bfs.in","neorientat")

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