# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numAdivinar = random.randint(0, 9)
print('Adiviná el número oculto entre el 0 y el 9')
userNum = -1
while userNum != numAdivinar:
    userNum = int(input('Inserta el número que creés que es: '))
    if (userNum == numAdivinar):
        print(f'Felicidades adivinaste! el número era {numAdivinar}.')
        quit()
    print('Fallaste, intentalo de nuevo.')