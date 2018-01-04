# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
def string(word):
    if word == word[0:1]:
        return word
    else:
        return  word[0] + '*' + string(word[1:])
print(string('hhxhhxhhxhh'))