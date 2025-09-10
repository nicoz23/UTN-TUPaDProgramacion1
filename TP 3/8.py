nombre = input('Ingrese su nombre: ')
opcion = int(input('Ingrese 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n'
                'Ingrese 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n'
                'Ingrese 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n'
                'Indique que opción desea: '))
match opcion:
    case 1:
        print(nombre.upper())
    case 2:
         print(nombre.lower())
    case 3:
         print(nombre.title())
    case _:
        print('Debes ingresar una opción correcta')