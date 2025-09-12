inputNum = input('Ingrese un número: ')
longitud = len(inputNum)
for x in range(longitud - 1, -1, -1):
    print(inputNum[x], end="")
