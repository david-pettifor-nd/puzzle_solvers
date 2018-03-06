import string
word_list_file = open('tools/words_alpha.txt', 'r')

word_list = []

for word in word_list_file:
    if word != '\n':
        w = (word.replace('\n', '').replace('\r', '')).lower()
        word_list.append(w)

word1 = 'dear'
word2 = 'sup'
word3 = 'dog'
word4 = 'came'

possible_word_answers = {
    'first': [],
    'second': [],
    'third': [],
    'fourth': []
}

# loop through each combination of two letters
for l1 in string.ascii_lowercase:
    for l2 in string.ascii_lowercase:
        # check first word
        if word1 + l1 + l2 in word_list:
            print("\tFound possible word for first entry: "+word1+l1+l2)
            possible_word_answers['first'].append(word1 + l1 + l2)

        # check second word
        if word2 + l1 + l2 in word_list:
            print("\tFound possible word for second entry: " + word2 + l1 + l2)
            possible_word_answers['second'].append(word2 + l1 + l2)

        # check third word
        if word3 + l1 + l2 in word_list:
            print("\tFound possible word for third entry: " + word3 + l1 + l2)
            possible_word_answers['third'].append(word3 + l1 + l2)

        # check fourth word
        if word4 + l1 + l2 in word_list:
            print("\tFound possible word for fourth entry: " + word4 + l1 + l2)
            possible_word_answers['fourth'].append(word4 + l1 + l2)

print("Possibilities exhausted...calculating solutions...")

# iterate through each list
solution_found = False
for s1 in possible_word_answers['first']:
    for s2 in possible_word_answers['second']:
        for s3 in possible_word_answers['third']:
            for s4 in possible_word_answers['fourth']:
                if s1[-2:] + s2[-2:] + s3[-2:] + s4[-2:] in word_list:
                    solution_found = True
                    print("\tAnswer found: "+s1[-2:]+s2[-2:]+s3[-2:]+s4[-2:])

if not solution_found:
    print("\tNo answer found.")
