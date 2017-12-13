
def anagram(first_word, second_word):
    first = sorted(first_word)
    second = sorted(second_word)
    if len(first) == len(second) and first[:] == second[:]:
        return True
    else: 
        return False