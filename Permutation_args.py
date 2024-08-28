import itertools


def execute_with_permutations(func, *args):
    # Générer toutes les permutations possibles des arguments
    permutations = itertools.permutations(args)

    # Exécuter la fonction pour chaque permutation
    results = []
    for perm in permutations:
        result = func(*perm)
        results.append((perm, result))

    return results


# Exemple de fonction à utiliser
def example_function(x, y, z, w):
    return x + y + z + w


# Exemple d'utilisation
if __name__ == "__main__":
    # Arguments de la fonction
    args = (1, 2, 3, 4)

    # Exécuter la fonction example_function avec toutes les permutations possibles des arguments
    results = execute_with_permutations(example_function, *args)

    # Afficher les résultats
    for perm, result in results:
        print(f"Arguments: {perm} => Résultat: {result}")
