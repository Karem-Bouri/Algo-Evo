import random


def calculer_distance(solution, distance_matrix):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance_matrix[solution[i]][solution[(i + 1)]]
    total_distance += distance_matrix[solution[-1]][solution[0]]
    return total_distance


def generer_mutation(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin


def selection_par_rang(population, distances):
    ranked_population = sorted(zip(population, distances), key=lambda x: x[1])
    total_ranks = sum(range(1, len(population) + 1))
    probabilities = [rank / total_ranks for rank in range(len(population), 0, -1)]
    return ranked_population[random.choices(range(len(population)), weights=probabilities)[0]][0]



def crossover_par_rang(population, distances):
    parent1 = selection_par_rang(population, distances)
    parent2 = selection_par_rang(population, distances)
    taille = len(parent1)
    start, end = sorted(random.sample(range(taille), 2))
    enfant = [None] * taille
    enfant[start:end] = parent1[start:end]
    pointer = 0
    for i in range(taille):
        if enfant[i] is None:
            while parent2[pointer] in enfant:
                pointer += 1
            enfant[i] = parent2[pointer]

    return enfant


def algorithme_genetique(distance_matrix, taille_population, taux_mutation, max_generations):
    nombre_villes = len(distance_matrix)
    population = []
    for _ in range(taille_population):
        solution = list(range(nombre_villes))
        random.shuffle(solution)
        population.append(solution)

    meilleure_solution = None
    meilleure_distance = float('inf')

    for generation in range(max_generations):
        distances = [calculer_distance(sol, distance_matrix) for sol in population]
        nouvelle_population = []

        for _ in range(taille_population):
            enfant = crossover_par_rang(population, distances)
            if random.random() < taux_mutation:
                enfant = generer_mutation(enfant)
            nouvelle_population.append(enfant)

        population = nouvelle_population

        for i in range(taille_population):
            dist = calculer_distance(population[i], distance_matrix)
            if dist < meilleure_distance:
                meilleure_distance = dist
                meilleure_solution = population[i][:]

    return meilleure_solution, meilleure_distance


# Exemple d'utilisation
if __name__ == "__main__":
    distance_matrix = [
        [0, 2, 2, 7, 15, 2, 5, 7, 6, 5],
        [2, 0, 10, 4, 7, 3, 7, 15, 8, 2],
        [2, 10, 0, 1, 4, 3, 3, 4, 2, 3],
        [7, 4, 1, 0, 2, 15, 7, 7, 5, 4],
        [7, 10, 4, 2, 0, 7, 3, 2, 2, 7],
        [2, 3, 3, 7, 7, 0, 1, 7, 2, 10],
        [5, 7, 3, 7, 3, 1, 0, 2, 1, 3],
        [7, 7, 4, 7, 2, 7, 2, 0, 1, 10],
        [6, 8, 2, 5, 2, 2, 1, 10, 0, 15],
        [5, 2, 3, 4, 7, 10, 3, 10, 15, 0]
    ]
    taille_population = 100
    taux_mutation = 0.1
    max_generations = 1000

    meilleure_solution, meilleure_distance = algorithme_genetique(distance_matrix,
                                                                  taille_population,
                                                                  taux_mutation,
                                                                  max_generations)
    print("Meilleure solution trouvée :", meilleure_solution)
    print("Distance de la meilleure solution :", meilleure_distance)