# sortarea topologica a unui graf orientat

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

def gradIntern(lista, n):

    grade = []

    for i in range (n):
        grad = 0
        for l in lista:
            if i + 1 in l:
                grad = grad + 1
        grade.append(grad)

    return grade

# functie care verifica daca o lista de liste e goala
def isEmpty(lista):
    for l in lista:
        if l != []:
            return False

    return True

def topologicalSort(lista, n):
    coada = []
    grade = gradIntern(lista, n)

    # adaugam in coada toate varfurile cu grad intern 0
    for i in range (n):
        if grade[i] == 0:
            coada.append(i + 1)

    # in coada vom pastra nodurile care au gradul
    # intern 0 si le vom elimina pe rand din graf
    index = 0
    while isEmpty(lista) == False:
        nod = coada[index]

        lista[nod - 1] = []

        # eliminam toate aparitiile nodului eliminat
        for i in range(len(lista)):
            if nod in lista[i]:
                lista[i].remove(nod)

        # actualizam lista cu gradele interne ale nodurilor
        grade = gradIntern(lista, n)

        # adaugam noile noduri cu grad intern 0
        for i in range (n):
            if grade[i] == 0 and (i + 1) not in coada:
                coada.append(i + 1)

        index = index + 1

    # procesul se opreste in momentul in care
    # graful este gol, adica lista de liste e goala
    
    return coada

lista = listaAdiacenta("graf.in", "orientat")

f = open("graf.in", "r")

n, m = [int(x) for x in f.readline().split()]

sortare = topologicalSort(lista, n)
print(sortare)

f.close()

