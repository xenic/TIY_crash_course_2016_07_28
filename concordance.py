from helper import clean_word
import operator
concordance = {}

f = open("data/alice_in_wonderland.txt", "r")
for line in f:
    #words becomes a list of all the words in line... separated by spaces
    words = line.lower().split()
    for word in words:
        word = clean_word(word)
        if word in concordance:
            concordance[word] = concordance[word] + 1
        else:
            concordance[word] = 1


#for word, count in sorted(concordance.items(), key=operator.itemgetter(1), reverse=True):
#    print(word, count)


user_in = input("What word are you looking for? ")
print(user_in, concordance[user_in])
