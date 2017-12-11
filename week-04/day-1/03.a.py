from nullaharom import Domino


def initialize_dominoes():
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = []
print(initialize_dominoes())

def sort(list):
    new_dominoeslist.append(dominoes[0])
    while len(new_dominoeslist) != len(dominoes):
        for i in range(1, len(dominoes)):
            if dominoes[i].values[0] == new_dominoeslist[-1].values[1]:
                new_dominoeslist.append(dominoes[i])  

new_dominoeslist = []
sort(dominoes)
print(new_dominoeslist)