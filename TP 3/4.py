edadInput = int(input('Ingrese su edad: '))

if (edadInput < 0):
    print('La edad no puede ser menor que 0')
    quit()

if (edadInput < 12):
    print('Niño/a')
elif (edadInput >= 12 and edadInput < 18):
    print('Adolescente')
elif (edadInput >= 18 and edadInput < 30):
    print('Adulto/a joven')
else:
    print('Adulto/a')

