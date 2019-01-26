print('Aprendiendo Python3')
clients = 'ronny,renzo,paul'
print('Valor de variable: ' + clients)

print('*' * 25 + ' FUNCIONES ' + '*' * 25)


def separator(title='', character='*'):
    """Esto es un texto de ayuda de como utilizar esta funcion. puede ser llamada con help(nombrefuncion)"""
    print('\n')  # salto de línea para la consola
    print('*' * 25 + title + '*' * 25)
    pass


# help(separator)


def create_client(client_name):  # Convención 2 espacios entre funciones
    global clients  # para traer una variable a entorno local
    _add_comma()
    clients += client_name


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, update_client_name + ',')
    else:
        print('Cliente no existe')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, '')
    else:
        print('Cliente no existe')


def _get_client_name():
    return input('Cual es el nombre del cliente?\n')


def _add_comma():
    global clients
    clients += ','  # concatenar en letras ó sumar en numéricos


def list_clients():
    print('Todos los clientes ==> ' + clients)


def _print_welcome():  # funciones que empiezan por subguión son privadas, las demás son públicas
    print('Welcome to python')
    print('#' * 50)
    list_clients()
    print('Seleccione una opción')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('#' * 50)
    print('\n\r')


x = 2  # asignación de variables
y = 3

if x < y:  # comparación simple
    print('x es menor que y')
else:
    print('x no es menor que y')

separator('JUGANDO CON STRINGS (CADENAS)')
country = 'Perú'
print('Mostrando una posición específica de la palabra: ' + country)
print(country[3])  # Muestra el caracter ú de la palabra Perú
print(country.upper())  # convertir en mayusculas
print(country.find('e'))  # devuelve posición inicial del caracter o palabra ingresada
print(country.startswith('p'))  # valida si el valor de la variable inicia con la letra p, aquí es true
print(country.startswith('x'))
print(dir(country))  # Muestra todas las funciones que pueden ser aplicadas.
# Las que tienen subguión permiten modificar como python se ejecuta
# las que no tienen subguión se pueden aplicar normalmente

separator('APLICACIÓN PRINCIPAL')

if __name__ == '__main__':
    _print_welcome()
    command = input()  # obtiene el valor ingresado por consola
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()  # Muestra texto y guarda valor ingresado por consola
        create_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('Por qué nombre desea cambiar?')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    else:
        print('Comando desconocido')
