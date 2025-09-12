cantidad = 10
par = 0
inpar = 0

for x in range(0, cantidad):
    inputNums = int(input('Ingrese el número: '))
    if (inputNums % 2 == 0):
        par += 1
    else:
        inpar += 1
print(f'Has ingreasado {par} números pares y {inpar} números inpares.')