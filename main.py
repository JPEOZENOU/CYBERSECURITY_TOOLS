import itertools
#import string


def generate_case_combination(word):
    char_options = [(char.lower(), char.upper()) for char in word]
    all_combinations = itertools.product(*char_options)
    result = [''.join(combination) for combination in all_combinations]
    return result

def generate_wordlist(words):
    wordlist = set()
    for word in words:
        permutations = [''.join(p) for p in itertools.permutations(word)]
        for perm in permutations:
            case_combinations = generate_case_combination(perm)
            wordlist.update(case_combinations)

    return list(wordlist)

if __name__ == '__main__':
    input_words = ['abc','def']
    wordlist = generate_wordlist(input_words)
    for word in wordlist:
        print(word)
