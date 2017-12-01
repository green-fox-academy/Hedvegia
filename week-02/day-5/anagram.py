inp1 = "fhjdsalhg"
inp2 = "fkdlsa"

s1 = sorted(inp1)
s2 = sorted(inp2)

def anagram (s1, s2):
    if len(s1) == len(s2):
        if  s1[:] == s2[:]:
            print(True)
        else:
            print(False)
    else: 
        print(False)

anagram(s1, s2)


