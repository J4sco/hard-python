from collections import Counter
import re

speech = []
sentence_list = []
end_charachers = ('.', '?', '!')
word_count = 0
punctuation_count = 0
phrase_count = 0
new_line = True

word = input("Start the speech: ")
word = word.strip()

while word.lower()!="stop":
    while (word not in end_charachers) and (word != ','):
        word_count += 1
        
        if not(new_line):
            sentence_list.append(word)
        else:
            sentence_list.append(word.capitalize())
            new_line = False
            phrase_count += 1

        word = input(">> ")
        word = word.strip()
    
    sentence = " ".join(sentence_list)
    sentence_list.clear()

    if word in end_charachers:
        sentence = sentence + word + "\n"
        new_line = True
    else:
        sentence = sentence + word + " "
    punctuation_count += 1

    speech.append(sentence)
    sentence = ""

    word = input(">> ")
    word = word.strip()
    
print("\n")

result = "".join(speech)
print(result)

print(("The speech is composed of {n} word(s) arranged in {N} sentence(s)").format(n=word_count, N=phrase_count))
print(("{} puntuation marks have ben used").format(punctuation_count))

most_common = Counter(c.lower() for c in re.findall(r"\w", result)).most_common(1)
print(("The most used caracter is '{}' with {} occurences").format(most_common[0][0], most_common[0][1]))

least_common = Counter(result)
least_common = min(least_common, key = least_common.get)
print(("The least used caracter is '{}'").format(least_common.lower()))