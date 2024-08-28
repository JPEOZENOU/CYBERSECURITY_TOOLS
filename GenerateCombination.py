import itertools

# Cette fonction permet d'obtenir l'ensemble des permuations possibles
# dont chaque element appartient à une liste différente. On ne peut pas
# avoir deux elements d'une même liste.
def generate_combinations(*word_lists):
    all_combinations = set()  # Using a set to avoid duplicate entries

    # Iterate over all possible numbers of lists (from 2 to the total number of lists)
    for r in range(2, len(word_lists) + 1):
        # Generate all combinations of lists of length r
        for list_combination in itertools.combinations(word_lists, r):
            # Generate all possible permutations of one word from each list in the combination
            for word_permutation in itertools.product(*list_combination):
                # Join the words to form a single string
                combined_word = ''.join(word_permutation)
                all_combinations.add(combined_word)

    return list(all_combinations)


def execute_with_permutations(func, *args):
    # Générer toutes les permutations possibles des arguments
    permutations = itertools.permutations(args)

    # Exécuter la fonction pour chaque permutation
    results = []
    for perm in permutations:
        result = func(*perm)
        results.append((perm, result))

    return results


# Cette fonction permet de stocker chaque mot d'une wordlist dans une liste
def read_words_from_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read lines from the file and strip whitespace
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def write_words_to_file(word_list, filename):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write each word on a new line
            for word in word_list:
                file.write(word + '\n')
        print(f"Words have been successfully written to '{filename}'")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":

    # File 01 : eca
    filename1 = 'eca'
    # Read the words from the file into a list
    word_list1 = read_words_from_file(filename1)
    # Print the list of words
    print("\nList of words from the file : eca\n")
    print(word_list1)

    # File 02 : ecadmin
    filename2 = 'ecadmin'
    # Read the words from the file into a list
    word_list2 = read_words_from_file(filename2)
    # Print the list of words
    print("\nList of words from the file : ecadmin\n")
    print(word_list2)

    # File 03 : exail
    filename3 = 'exail'
    # Read the words from the file into a list
    word_list3 = read_words_from_file(filename3)
    # Print the list of words
    print("\nList of words from the file : exail\n")
    print(word_list3)

    # File 04 : root
    filename4 = 'root'
    # Read the words from the file into a list
    word_list4 = read_words_from_file(filename4)
    # Print the list of words
    print("\nList of words from the file : root\n")
    print(word_list4)

    # File 05 : etoile
    filename5 = 'etoile'
    # Read the words from the file into a list
    word_list5 = read_words_from_file(filename5)
    # Print the list of words
    print("\nList of words from the file : etoile\n")
    print(word_list5)

    # File 06 : exclamation
    filename6 = 'exclamation'
    # Read the words from the file into a list
    word_list6 = read_words_from_file(filename6)
    # Print the list of words
    print("\nList of words from the file : exclamation\n")
    print(word_list6)

    # File 07 : exclamation
    filename7 = 'exclamation'
    # Read the words from the file into a list
    word_list7 = read_words_from_file(filename7)
    # Print the list of words
    print("\nList of words from the file : exclamation\n")
    print(word_list7)






    #allwords = generate_combinations(word_list1, word_list3, word_list5, word_list6)
    args = (word_list1, word_list3, word_list5, word_list6)
    allwords = execute_with_permutations(generate_combinations, *args)
    print(allwords)
    write_words_to_file(allwords, "Dico.txt")











