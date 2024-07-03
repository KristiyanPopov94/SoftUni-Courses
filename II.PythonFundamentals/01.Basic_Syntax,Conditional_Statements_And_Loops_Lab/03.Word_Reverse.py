word = input()
word_reversed = ''

for i in range(len(word) - 1, -1, -1):
    word_reversed += word[i]

print(word_reversed)


# word_reversed = word[::-1]
#
# print(word_reversed)