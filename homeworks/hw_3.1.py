from prettytable import PrettyTable 

table = PrettyTable()
table.field_names = ["Metric", "Value"]

speech = []
sentence_list = []
end_charachers = ('.', '?', '!')
word_count = 0
punctuation_count = 0
phrase_count = 0
new_line = True

word = input("Start the speech: ")
word = word.strip()
sentence = ""

while word.lower()!="stop":
    #if is a proper word
    if (word not in end_charachers) and (word != ','): 
        word_count += 1
        
        if not(new_line):
            sentence_list.append(word)
        else:
            sentence_list.append(word.capitalize())
            new_line = False
            phrase_count += 1

        #word = input(">> ")
        #word = word.strip()
    
    #sentence = " ".join(sentence_list)
    #sentence_list.clear()

    elif word in end_charachers:
        sentence = " ".join(sentence_list)
        sentence = sentence + word + "\n"
        new_line = True
        
        sentence_list.clear()
        punctuation_count += 1

    else:
        sentence = sentence + word + " "
        sentence = " ".join(sentence_list)

        sentence_list.clear()
        punctuation_count += 1

    speech.append(sentence)
    sentence = ""

    word = input(">> ")
    word = word.strip()
    
print("\n")

print("The input speech is:")
result = "".join(speech)
print(result)

#print(("The speech is composed of {n} word(s) arranged in {N} sentence(s)").format(n=word_count, N=phrase_count))
#print(("{} puntuation marks have ben used").format(punctuation_count))

#finding most and least frequent character
letters_dict = {}   #dictionary with letters occurences
for char in result.lower():
    if char not in ["\n", " "]:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1

max_char_count = max(letters_dict.values()) #max occurences number
min_char_count = min(letters_dict.values()) #min occurences number

most_frequent_chars = []  #list for the most frequent chars
least_frequent_chars = []  #list for the least frequent chars

for k, v in letters_dict.items():
    if v == max_char_count:
        most_frequent_chars.append(k)
    if v == min_char_count:
        least_frequent_chars.append(k)

table.add_row(["Number of words", word_count])
table.add_row(["Number of sentences", phrase_count])
table.add_row(["Number of puntuation marks", punctuation_count])
table.add_row(["Most used character(s) ({} occurence(s))".format(max_char_count), ", ".join(most_frequent_chars)])
table.add_row(["Least used character(s) ({} occurence(s))".format(min_char_count), ", ".join(least_frequent_chars)])

print("Speech analysis:")
print(table)