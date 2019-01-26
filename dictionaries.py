import sys

# Diccionarios forma 2

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }
]


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('Ingrese el {}\n'.format(field_name))

    return field


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('El cliente {} ya existe'.format(client.get('name')))


def list_clients():
    global clients
    for idx, client in enumerate(clients):  # con enumarate se puede traer el índice
        print('{uid} | {name} | {company} | {email} | {position}'.format(uid=idx, name=client['name'],
                                                                         company=client['company'],
                                                                         email=client['email'],
                                                                         position=client['position']))


def update_client(_type, value, new_value):
    global clients

    for index, client in enumerate(clients):
        _type = str(_type).strip()
        if client.get(_type) == value:
            clients[index][_type] = new_value
            print('Valor {} actualizado'.format(_type))
            break

    print('Cliente no existe')


def _get_index_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            print('indice {}'.format(idx))
            return idx
    print('No existe el cliente')


def delete_client(client_id):
    global clients
    for index, client in enumerate(clients):
        if int(client_id) == index:
            print('Eliminado cliente {}'.format(client_id))
            del clients[index]
            break


def search_client(by, valor):
    global clients

    for idx, client in enumerate(clients):
        if client.get(by) == valor:
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
    print('#' * 50)
    print('Seleccione una opción')
    print('[L]ist clients')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('#' * 50)
    print('\n\r')


def dict_application():
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        new_client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(new_client)
    elif command == 'U':
        _type = _get_client_field('tipo')
        valor = _get_client_field('Valor actual')
        new_value = input('Nuevo valor')
        update_client(_type, valor, new_value)
    elif command == 'D':
        client_id = _get_client_field('id')
        delete_client(client_id)

    elif command == 'S':
        by = _get_client_field('columna')
        valor = _get_client_field('Valor actual')
        found = search_client(by, valor)
        if found:
            print('Cliente encontrado!')
        else:
            print('{}, {} no ha sido encontrado'.format(by, valor))
    elif command == 'L':
        list_clients()
    else:
        print('Comando desconocido')
    dict_application()


if __name__ == '__main__':
    dict_application()
