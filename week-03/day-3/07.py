# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
def string(word, x, y):
    if word == '':
        return word
    else:
        if word[0] == x:
            return y + string(word[1:], x, y)
        else:
            return word[0] + string(word[1:], x, y)
print(string('hhxhhxhhxhh', 'x', 'y'))