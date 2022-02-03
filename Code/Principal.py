
def principalmenu():
    continue = True
    while continue:
        correctoption = False
        while not correctoption:
            print('MENÚ PRINCIPAL')
            print('1.Listar Marcas')
            print('2.Registrar Marcas')
            print('3.Actualizar Marcas')
            print('4.Eliminar Marcas')
            print('5.Salir')
            option = int(input('Seleccione una opción: '))

            if option < 1 or option > 5:
                print('Opción incorrecta, ingrese nuevamente')
            elif option == 5:
                continue = False
                print('Gracias por usar este sistema.')
            else:
                correctoption = True
                execoption(option)


def execoption(option):
    print(option)

principalmenu()
