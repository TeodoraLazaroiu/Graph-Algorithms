# Scrieți un subprogram pentru construirea în memorie a listelor de adiacență
# pentru un graf - neorientat/orientat în funcție de un parametru trimis
# subprogramului, citit din fișierul graf.in cu structura precizată
# mai sus și un subprogram pentru afișarea listelor de adiacență

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


def afisareLista(lista):

    n = int(len(lista))

    for i in range(n):
        print(f"{i+1}: {sorted(lista[i])}")