import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ')
        print('-' * 60)
        os.system('ping -n 3 {}' .format(ip))
        print('-' * 60)
        time.sleep(5)

