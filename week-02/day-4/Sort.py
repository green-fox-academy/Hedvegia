inp = [34, 12, 24, 9, 5]

def sort (ls):
    for i in inp:
        for n in inp:
            if i >= n:
                vars = n
                n = i
                i = vars
            else:
                pass
    return inp
                
print(sort(inp))
         