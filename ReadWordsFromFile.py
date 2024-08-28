# Ce script permet de stocker chaque mot d'une wordlist dans une liste

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














