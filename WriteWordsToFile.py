

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
    # Define a list of words
    words = ['apple', 'banana', 'cherry', 'date']

    # Specify the name of the text file to write to
    filename = 'output_wordlist.txt'

    # Write the words to the file
    write_words_to_file(words, filename)
