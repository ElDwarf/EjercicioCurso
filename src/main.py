import json
import requests


def send_petition(nombre, apellido)
    url_base = 'https://4etjz3ty75.execute-api.us-east-1.amazonaws.com/default/curso_step_1'
    url = url_base + '?nombre={0}&apellido={1}'.format(nombre, apellido)
    r = requests.get(url)
    content_json = json.loads(r.content)
    print()
    print('Tarea:')
    print(content_json['tarea'])
    print('URL:')
    print(content_json['url'])


if __name__ == '__main__':
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    send_petition(nombrecompleto, apellido)
