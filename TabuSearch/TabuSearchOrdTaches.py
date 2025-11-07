import random
from collections import deque

def calculer_cout(solution, cout_matrix):
    total_cout = 0
    for i in range(len(solution)-1):
        total_cout += cout_matrix[solution[i]][solution[(i + 1)]]
    return total_cout

def generer_voisin(solution):
    voisins = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

def tabu_search(cout_matrix, tabu_size, max_iterations):
    nombre_taches = len(cout_matrix)
    solution_courante = list(range(nombre_taches))
    random.shuffle(solution_courante)

    meilleure_solution = solution_courante[:]
    meilleure_cout = calculer_cout(meilleure_solution, cout_matrix)

    tabu_list = deque(maxlen=tabu_size)


    for _ in range(max_iterations):
        voisins = generer_voisin(solution_courante)
        voisins = [voisin for voisin in voisins if voisin not in tabu_list]
        if not voisins:
            break

        solution_courante = min(voisins,key=lambda x: calculer_cout(x, cout_matrix))
        cout_courante= calculer_cout(solution_courante, cout_matrix)

        tabu_list.append(solution_courante)

        if cout_courante< meilleure_cout:
            meilleure_solution = solution_courante[:]
            meilleure_cout = cout_courante

    return meilleure_solution, meilleure_cout


# Exemple d'utilisation
if __name__ == "__main__":
    cout_matrix = [
        [0,10,16,8,18],
        [10,0,9,15,21],
        [16,9,0,7,12],
        [8,15,7,0,12],
        [18,21,12,12,0]

    ]

    max_iterations = 1000
    tabu_size = 50

    meilleure_solution, meilleure_cout = tabu_search(cout_matrix, tabu_size, max_iterations)
    print("Meilleure solution trouvée :", meilleure_solution)
    print("Cout de la meilleure solution :", meilleure_cout)