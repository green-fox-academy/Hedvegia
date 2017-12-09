#Create a function that takes two strings as a parameter
#Returns the starting index where the second one is starting in the first one
#Returns -1 if the second string is not in the first one
#Example

#input: "this is what I'm searching in", "searching"
#output: 17

def searching(sentence, word):
    listed_sentence = sentence.split()
    output = 0
    for i in range(0, len(listed_sentence)):
        if word == listed_sentence[i]:
            return output
        else:
            output += len(listed_sentence[i])+1
    if output == len(sentence)+1:
        return -1

s = "this is what I'm searching in"
w = "this"
print(searching(s, w))