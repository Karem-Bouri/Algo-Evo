import random
def calculer_distance(solution, distance_matrix):
    total_distance = 0
    for i in range(len(solution)-1):
        total_distance += distance_matrix[solution[i]][solution[(i + 1)]]
    total_distance += distance_matrix[solution[-1]][solution[0]]
    return total_distance

def generer_voisin(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin

def recuit_simule(distance_matrix, initial_temp, cooling_rate, max_iterations):
    nombre_villes=len(distance_matrix)
    solution_courante = list(range(nombre_villes))
    random.shuffle(solution_courante)

    meilleure_solution = solution_courante[:]
    meilleure_distance = calculer_distance(meilleure_solution, distance_matrix)
    temperature = initial_temp
    iteration = 0

    while iteration < max_iterations:

        voisin=generer_voisin(solution_courante)
        distance_courante = calculer_distance(solution_courante, distance_matrix)
        distance_voisin = calculer_distance(voisin, distance_matrix)

        if temperature==0:
            break
        if distance_voisin < distance_courante or random.uniform(0, 1) < pow(2.71828, -(distance_voisin - distance_courante) / temperature):
            solution_courante=voisin[:]
            distance_courante=distance_voisin
            if distance_courante < meilleure_distance:
                meilleure_solution = solution_courante[:]
                meilleure_distance = distance_courante
        temperature *= cooling_rate
        iteration += 1
    return meilleure_solution, meilleure_distance


# Exemple d'utilisation
if __name__ == "__main__":
    distance_matrix = [
        [0,2,2,7,15,2,5,7,6,5],
        [2,0,10,4,7,3,7,15,8,2],
        [2,10,0,1,4,3,3,4,2,3],
        [7,4,1,0,2,15,7,7,5,4],
        [7,10,4,2,0,7,3,2,2,7],
        [2,3,3,7,7,0,1,7,2,10],
        [5,7,3,7,3,1,0,2,1,3],
        [7,7,4,7,2,7,2,0,1,10],
        [6,8,2,5,2,2,1,10,0,15],
        [5,2,3,4,7,10,3,10,15,0]
    ]
    initial_temp = 10000
    cooling_rate = 0.995
    max_iterations = 100000

    meilleure_solution, meilleure_distance = recuit_simule(distance_matrix, initial_temp, cooling_rate, max_iterations)
    print("Meilleure solution trouvée :", meilleure_solution)
    print("Distance de la meilleure solution :", meilleure_distance)