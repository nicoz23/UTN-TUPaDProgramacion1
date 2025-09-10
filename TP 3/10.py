hemisferio = input('¿En que hemisferio te encuentras?\n' \
                    'Ingrese N si te encuentras en el hemisferio norte\n' \
                    'Ingrese S si te encuentras en el hemisferio sur\n' \
                    'Opción: ').lower()
mes = int(input('Ingrese en número en que mes del año te encuentras: '))
dia = int(input('Ingrese que día es hoy (número): '))
estacion = ''

if (hemisferio == 'n'):
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia < 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 20) or (mes <= 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia < 22):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif (hemisferio == 's'):
    if (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia < 22):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 22) or (mes <= 11) or (mes == 12 and dia < 21):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia < 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    print('Debe ingresar correctamente un hemisferio.')

print("Estación:", estacion)
