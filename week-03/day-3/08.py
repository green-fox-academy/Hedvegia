# Given a string, compute recursively a new string where all the 'x' chars have been removed.
def string(word, x, y):
    if word == '':
        return word
    else:
        if word[0] == x:
            return  string(word[1:], x, y)
        else:
            return word[0] + string(word[1:], x, y)
print(string('hhxhhxhhxhh', 'x', 'y'))