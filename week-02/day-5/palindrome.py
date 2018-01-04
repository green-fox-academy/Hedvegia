inp1 = input("enter a word: ")

def create_palindrome (inp1):
    print(inp1[0:] + inp1[::-1])

create_palindrome(inp1)