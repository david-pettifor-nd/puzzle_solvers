word_list_file = open('tools/words_alpha.txt', 'r')

three_letter_word_list = []
four_letter_word_list = []
all_words = []

for word in word_list_file:
    if word != '\n':
        w = (word.replace('\n', '').replace('\r', '')).lower()
        if len(w) == 3:
            three_letter_word_list.append(w)
        if len(w) == 4:
            four_letter_word_list.append(w)
        all_words.append(w)


word1 = 'fun'
word2 = 'way'
word3 = 'car'
word4 = 'ace'

print("Searching for first missing word....")
# run through each four letter word and see if appending it to word1 forms a new word
for w in four_letter_word_list:
    if word1 + w in all_words:
        # does w + word2 make a word?
        if w + word2 in all_words:
            print("\tFound answer for first word: "+w)

print("\nSearching for second missing word...")
# now how about words 2 and 3?
for w in four_letter_word_list:
    if word2 + w in all_words and w + word3 in all_words:
        print("\tFound answer for second word: "+w)


print("\nSearching for third missing word...")
# now how about words 3 and 4?
for w in three_letter_word_list:
    if word3 + w in all_words and w + word4 in all_words:
        print("\tFound answer for third word: "+w)