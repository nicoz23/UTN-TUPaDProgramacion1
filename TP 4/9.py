
from statistics import mean
cantidad = 10
nums = []
for x in range(0, cantidad):
    inputNums = int(input('Ingresa un número: '))
    nums.append(inputNums)
print(f'La media de los números ingresados es: {mean(nums)}')