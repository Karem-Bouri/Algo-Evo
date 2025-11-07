import random
def calculer_cout(solution, cout_matrix):
    total_cout = 0
    for i in range(len(solution)-1):
        total_cout += cout_matrix[solution[i]][solution[(i + 1)]]

    return total_cout

def generer_mutation(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin

def selection_par_rang(population, couts):
    ranked_population = sorted(zip(population, couts), key=lambda x: x[1])
    total_ranks = sum(range(1, len(population) + 1))
    probabilities = [rank / total_ranks for rank in range(len(population), 0, -1)]
    return ranked_population[random.choices(range(len(population)), weights=probabilities)[0]][0]

def crossover_par_rang(population, couts):
    parent1 = selection_par_rang(population, couts)
    parent2 = selection_par_rang(population, couts)
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

def algorithme_genetique(cout_matrix, taille_population, taux_mutation, max_generations):
    nombre_taches = len(cout_matrix)
    population = []
    for _ in range(taille_population):
        solution = list(range(nombre_taches))
        random.shuffle(solution)
        population.append(solution)

    meilleure_solution = None
    meilleur_cout = float('inf')

    for generation in range(max_generations):
        couts = [calculer_cout(sol, cout_matrix) for sol in population]
        nouvelle_population = []

        for _ in range(taille_population):
            enfant = crossover_par_rang(population, couts)
            if random.random() < taux_mutation:
                enfant = generer_mutation(enfant)
            nouvelle_population.append(enfant)

        population = nouvelle_population

        for i in range(taille_population):
            cout_actuel = calculer_cout(population[i], cout_matrix)
            if cout_actuel < meilleur_cout:
                meilleure_solution = population[i][:]
                meilleur_cout = cout_actuel

    return meilleure_solution, meilleur_cout

# Exemple d'utilisation
if __name__ == "__main__":
    cout_matrix = [
        [0,10,16,8,18],
        [10,0,9,15,21],
        [16,9,0,7,12],
        [8,15,7,0,12],
        [18,21,12,12,0]

    ]
    taille_population = 100
    taux_mutation = 0.1
    max_generations = 500

    meilleure_solution, meilleur_cout = algorithme_genetique(cout_matrix, taille_population, taux_mutation, max_generations)
    print("Meilleure solution trouvée :", meilleure_solution)
    print("Cout de la meilleure solution :", meilleur_cout)