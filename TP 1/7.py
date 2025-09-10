num1 = int(input('Escribe el 1er número: '))
num2 = int(input('Escribe el 2do número: '))

while num1 == 0 or num2 == 0:
    print('El/los números ingresados no pueden ser cero.')
    num1 = int(input('Escribe el 1er número: '))
    num2 = int(input('Escribe el 2do número: '))
    continue

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} x {num2} = {num1 * num2}')


