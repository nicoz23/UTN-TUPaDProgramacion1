from statistics import mode, median, mean
import random

numRandom = [random.randint(1,100) for i in range(50)]
moda = mode(numRandom)
mediana = median(numRandom)
media = mean(numRandom)

print(f'Según está lista de números: {numRandom}')
print(f'Su moda es: {moda}')
print(f'Su mediana es: {mediana}')
print(f'Su media es: {media}')

if (media > mediana > moda):
    print('Sesgo positivo')
elif (media < mediana < moda):
    print('Sesgo negativo')
else:
    print('Sin sesgo')