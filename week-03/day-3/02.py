# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def counts(n):
    if 1 >= n: 
        return n
    else:
        return n + counts(n-1)
print(counts(12)) 