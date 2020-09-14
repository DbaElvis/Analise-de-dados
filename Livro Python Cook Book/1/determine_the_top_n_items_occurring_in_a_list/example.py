from collections import Counter

# example.py
#
# Determine the most common words in a list


words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]


word_counts = Counter(words)

top_three = word_counts.most_common(4)

print('Primeiro print')

print(top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]


print('\n')

# Example of merging in more words

morewords = ['why','are','you','not','looking','in','my','eyes']

word_counts.update(morewords)

print('Segundo print')

print(word_counts.most_common(3))



teste = "Determine the most a a a common words in a list No código acima, definimos uma String e dentro desta, colocamos uma marcação aa, somente para facilitar o estudo. Em seguida, invocamos a funçao replace(), e dissemos, que queríamos alterar a string aa pelo texto Feito isso, uma nova String foi retornada, com a alteração feita."

a = teste.split(" ")

b = Counter(a)

c = b.most_common()

for d in c:
      print(d)


