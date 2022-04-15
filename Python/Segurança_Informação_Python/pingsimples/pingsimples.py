import os #Importa o modulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 120)##Imprimindo #120 vezes

ip_ou_host =  input('Digite o IP ou host a ser verificado: ')#Criamos uma variavel que vai receber do usuario um IP
print("-" * 120)##Imprimindo #120 vezes
os.system('ping -n 4 {}'.format(ip_ou_host))##Chamando system da biblioteca os - comando ping #-n -num de pacotes que serão 4 {}
print("_" * 120)##Imprimindo #120 vezes