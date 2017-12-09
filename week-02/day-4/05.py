#Create a function that takes a string and a list of string as a parameter
#Returns the index of the string in the list where the first string is part of
#Returns -1 if the string is not part any of the strings in the list
#Example

# én egy listát adok vissza, mert lehet több találat is. 

def find_my_word(lst, word):
    out = []
    for i in range(len(lst)):
        if word in lst[i]:
            out.append(i)
    return out

inp = ["this", "is", "what", "I'm", "searching", "in"]
word = "is"
print(find_my_word(inp, word))