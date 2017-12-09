
# Függvény, mely kiírja egy számról, hogy Armstrong-szám-e
# @param input : a szám, amiről meg kell állapítani, hogy .. 
def armstrong(input):
    summa = 0
    originalInput = input
    inputString = str(input)

    # Mindig az utolsó számjegyet emeljük a kellő hatványra, ehhez tízzel való maradékos osztást végzünk. 
    while input != 0:
        number = input % 10
        summa += number ** len(inputString)
        input = input // 10
        
    if summa == originalInput:
        print('The', originalInput, 'is an Armstrong number')
    else:
        print('This is not an Armstrong number')

#Próba
armstrong(int(input('Enter a number: ')))

