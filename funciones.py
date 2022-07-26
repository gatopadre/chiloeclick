lista = [
    {'id': 1, 'name':'Le Chinchel', 'category':'Pub', 'url': 'http://127.0.0.1:8080/', 'status': 1},
    {'id': 2, 'name':'El Cantino', 'category':'Pub', 'url': 'http://127.0.0.1:8080/', 'status': 1},
    {'id': 3, 'name':'El Jardin Techado', 'category':'Pub', 'url': 'http://127.0.0.1:8080/', 'status': 1},
    {'id': 4, 'name':'Le Chinchel', 'category':'Pub', 'url': 'http://127.0.0.1:8080/', 'status': 1},
]

def get_data():
    return lista

if __name__ == '__main__':
    print(get_data(), len(get_data()))