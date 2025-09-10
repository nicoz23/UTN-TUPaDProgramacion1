password = input('Ingrese su contraseña (entre 8 y 14 caracteres): ')
if (len(password) >= 8 and len(password) <= 14):
    print(f'Ha ingresado una contraseña correcta. {len(password)} caracteres.')
else:
    print(f'Por favor, ingrese una contraseña de entre 8 y 14 caracteres. {len(password)} caracteres.')