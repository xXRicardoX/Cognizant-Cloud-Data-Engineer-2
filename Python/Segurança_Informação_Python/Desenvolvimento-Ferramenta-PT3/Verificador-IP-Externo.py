import re
import json
from urllib.request import  urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao =  dados['region']

print('detalhes do IP externo\n')
print('ip: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'.format(org,regiao,pais,cid,ip))