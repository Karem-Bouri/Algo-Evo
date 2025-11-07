import random
def calculer_cout(solution, cout_matrix):
    total_cout = 0
    for i in range(len(solution)-1):
        total_cout += cout_matrix[solution[i]][solution[(i + 1)]]

    return total_cout

def generer_voisin(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin

def recuit_simule(cout_matrix, initial_temp, cooling_rate, max_iterations):
    nombre_taches=len(cout_matrix)
    solution_courante = list(range(nombre_taches))
    random.shuffle(solution_courante)

    meilleure_solution = solution_courante[:]
    meilleure_cout = calculer_cout(meilleure_solution, cout_matrix)
    temperature = initial_temp
    iteration = 0

    while iteration < max_iterations:

        voisin=generer_voisin(solution_courante)
        cout_courante = calculer_cout(solution_courante, cout_matrix)
        cout_voisin = calculer_cout(voisin, cout_matrix)

        if temperature==0:
            break
        if cout_voisin < cout_courante or random.uniform(0, 1) < pow(2.71828, -(cout_voisin - cout_courante) / temperature):
            solution_courante=voisin[:]
            cout_courante=cout_voisin
            if cout_courante < meilleure_cout:
                meilleure_solution = solution_courante[:]
                meilleure_cout = cout_courante
        temperature *= cooling_rate
        iteration += 1
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
    initial_temp = 10000
    cooling_rate = 0.995
    max_iterations = 1000

    meilleure_solution, meilleure_cout = recuit_simule(cout_matrix, initial_temp, cooling_rate, max_iterations)
    print("Meilleure solution trouvée :", meilleure_solution)
    print("Cout de la meilleure solution :", meilleure_cout)