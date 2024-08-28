import itertools
# ce script permet à partir d'un seul mot, d'en générer toutes les versions
# et de les afficher à l'ecran dans un premier temps.
# On execute le script individuellement pour chaque mot que l'on veut traiter

def generate_case_combinations(word):
    # Create a list of character sets: lowercase and uppercase for each letter
    char_options = [(char.lower(), char.upper()) for char in word]

    # Use itertools.product to generate all combinations
    all_combinations = itertools.product(*char_options)

    # Join each tuple into a string
    result = [''.join(combination) for combination in all_combinations]

    return result

def write_words_to_file(word_list, filename):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write each word on a new line
            for word in word_list:
                file.write(word + '\n')
        # print(f"Words have been successfully written to '{filename}'")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# Example usage
word = 'administrator'
combinations = generate_case_combinations(word)

# Print the results
for combo in combinations:
    print(combo)

# Define a list of words

    # Specify the name of the text file to write to
    filename = "administrator.txt"

    # Write the words to the file
    write_words_to_file(combinations, filename)
