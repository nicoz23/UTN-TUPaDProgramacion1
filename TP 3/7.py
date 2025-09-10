frase = input('Ingrese una frase: ')
lenght = len(frase)
ultimaLetra = frase[lenght-1]
vocal = ['a', 'e', 'i', 'o', 'u']

for i in vocal:
    if (ultimaLetra == i):
        print(f'{frase}!')
        quit()

print(frase)