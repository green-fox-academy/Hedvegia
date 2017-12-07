# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def recursive(n, x):
    if x <= 1:
        return n
    else:
        return recursive(n, x-1) * n
print(recursive(2, 10))