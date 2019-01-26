import sys

clients = ['Lennon', 'McCartney', 'Starr', 'Harrison']  # array

# Diccionarios forma 1
rae = {}
rae['pizza'] = 'Comida italiana redonda'
rae['pasta'] = 'Comida italiana con fideos'

print(rae['pasta'])  # mostrar valor de la llave pasta
print(rae.get('vino', 'bebida de los dioses'))  # la funcion get tiene un valor por defecto
print(rae.get('pasta', 'fideos'))
print(dir(rae))
print('#' * 50)


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('El cliente {} ya existe'.format(client_name))


def list_clients():
    for idx, client in enumerate(clients):  # con enumarate se puede traer el índice
        print('{}:{}'.format(idx, client))


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('Cliente no existe')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.remove(client_name)
    else:
        print('Cliente no existe')


def search_client(client_name):
    global clients

    for client in clients:
        if client == client_name:
            return True
        else:
            continue


def _get_client_name():
    client_name = None  # variable seteada como vacía
    while not client_name:
        client_name = input('Cual es el nombre del cliente?\n')
        if client_name == 'exit':
            break
    if client_name == 'exit':
        sys.exit()
    return client_name


def _print_welcome():  # funciones que empiezan por subguión son privadas, las demás son públicas
    print('Welcome to python')
    print('#' * 50)
    list_clients()
    print('Seleccione una opción')
    print('[L]ist clients')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('#' * 50)
    print('\n\r')


def first_application():
    _print_welcome()
    command = input()  # obtiene el valor ingresado por consola
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()  # Muestra texto y guarda valor ingresado por consola
        create_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('Por qué nombre desea cambiar?')
        update_client(client_name, updated_client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('Cliente encontrado!')
        else:
            print('Cliente {} no ha sido encontrado'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Comando desconocido')
    first_application()


if __name__ == '__main__':
    first_application()
