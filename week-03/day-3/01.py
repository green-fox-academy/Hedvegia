# Write a recursive function that takes one parameter: n and counts down from n.

def counts(n):
    if n <= 1: 
        return 1
    else:
        return n + counts(n-1)
print(counts(10))