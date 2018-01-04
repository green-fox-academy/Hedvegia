# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif c > b and c > a:
        return c
    else:
        return b

# Returns the median value of a list given as param
def median(pool):
    median = 0
    for i in pool:
        median += i
    return median / len(pool)

# Returns true if the param is a vovel
def is_vovel(char):
    vovels = ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú", "ü", "ű"]
    if char.lower() in vovels:
        return True
    else: 
        return False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve