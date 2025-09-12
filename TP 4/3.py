num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
suma = 0

for x in range(num1+1,num2):
    suma += x
print(suma)