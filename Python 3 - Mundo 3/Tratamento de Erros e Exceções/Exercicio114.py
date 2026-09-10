# # Verificar se um site está acessível
#
# from urllib import request, error
#
# try:
#     site = request.urlopen('https://www.pudim.com.br/')
# except error.URLError:
#     print('\033[0;31mO site PUDIM não esta acessivel no momento!\033[m')
# else:
#     print('\033[0;32mConsegui acessar o site PUDIM com sucesso!\033[m')

# Verificar qual erro esta acontecendo

# from urllib import request, error
#
# try:
#     site = request.urlopen('https://www.pudim.com.br/')
# except error.URLError as erro:
#     print('\033[0;31mO site PUDIM não esta acessivel no momento!\033[m')
#     print(erro)
# else:
#     print('\033[0;32mConsegui acessar o site PUDIM com sucesso!\033[m')

# Testando outro site
from urllib import request, error

try:
    site = request.urlopen('https://www.google.com')
except error.URLError as erro:
    print(f'\033[0;31mNão consegui acessar o site!\033[m')
    print(erro)
else:
    print('\033[0;32mConsegui acessar o site com sucesso!\033[m')