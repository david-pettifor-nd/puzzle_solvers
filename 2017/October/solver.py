import string

word_list_file = open('tools/words_alpha.txt', 'r')

word_list = []

for word in word_list_file:
    if word != '\n':
        w = (word.replace('\n', '').replace('\r', '')).lower()
        word_list.append(w)

first_entry = ['BASIC', 'RELIT']
second_entry = ['PASTE', 'CHINK']
third_entry = ['THERE', 'BREAD']
fourth_entry = ['CRANK', 'PLANK']
fifth_entry = ['DROOP', 'CREEP']


def find_possible_words(entry):
    possible_answers = []
    # for the first entry, loop through the alphabet...
    for letter in string.ascii_lowercase:
        new_word = (entry[0][:-1] + letter).lower()
        if new_word in word_list:
            # can we make a valid word with the second part of our entry?
            new_word = (entry[1][:-1] + letter).lower()
            if new_word in word_list:
                possible_answers.append(letter)

    return possible_answers


def assemble_words(compiled_word, remaining_choices):
    if len(remaining_choices) == 0:
        # is the compiled word a valid word?
        if compiled_word.lower() in word_list:
            print "ANSWER FOUND: ", compiled_word.lower()
            return
    else:
        next_group = remaining_choices[0]
        for choice in next_group:
            assemble_words(compiled_word + choice, remaining_choices[1:])

choices = []
choices.append(find_possible_words(first_entry))
choices.append(find_possible_words(second_entry))
choices.append(find_possible_words(third_entry))
choices.append(find_possible_words(fourth_entry))
choices.append(find_possible_words(fifth_entry))

assemble_words('', choices)
