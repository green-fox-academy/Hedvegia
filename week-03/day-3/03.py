# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

non_n = int(input('Give a non-negative number: '))
def counts(non_n):
    a = non_n % 10
    if non_n <= 0:
        return non_n
    else: 
        return counts(non_n // 10) + a
print(counts(non_n))