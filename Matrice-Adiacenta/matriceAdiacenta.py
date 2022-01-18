# Scrieți un subprogram pentru construirea în memorie a matricei de adiacență
# a unui graf - neorientat/orientat în funcție de un parametru trimis
# subprogramului, citit din fișierul graf.in cu structura precizată
# mai sus și un subprogram pentru afișarea matricei de adiacență

import math

def matriceAdiacenta(fisier, orientare):
    f = open(fisier)

    n = int(f.readline().split()[0])

    matrice = [0 for _ in range(n * n)]

    if orientare == "neorientat" or orientare == "orientat":
        for linie in f:
            i, j = [int(x) for x in linie.split()]

            matrice[(i-1) * n + j-1] = 1

            if orientare == "neorientat":
                matrice[(j-1) * n + i-1] = 1
    else:
        exit("Orientarea grafului este gresita")

    f.close()

    return matrice

def afisareMatrice(matrice):

    n = int(math.sqrt(len(matrice)))

    for i in range(n):
        for j in range(n):
            print(matrice[i * n + j], end=" ")
        print()