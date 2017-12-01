inp = [1, 11, 34, 11, 52, 61, 1, 34]
new_inp = []

def each_number (ls):
    for i in inp:
        if i not in new_inp:
            new_inp.append(i)
    return new_inp

print(each_number(new_inp))
