#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
print('\033[0;0;36m-=\033[m'*20)
print('Alistamento militar')
print('\033[0;0;36m-=\033[m'*20)
ano = int(input('Digite aqui o seu ano de nascimento com os quatro digitos: '))
print('\033[1;0;35mVerificando...\033[m')
sleep(1)
idade = abs(ano - date.today().year)
idade2 = abs(ano + 18)
print('\033[1;0;36mVocê está com {} anos.\033[m'.format(idade))
if idade > 18:
    print('\033[0;0;34mJá passou da idade!\033[m')
    print('\033[1;0;34mSeu alistamento foi em {}.'.format(idade2))
elif idade == 18:
    print('\033[0;0;33mEstá na hora certa! Procure uma junta militar.\033[m')
else:
    print('\033[0;0;32mAinda não chegou seu tempo.\033[m')
    print('\033[1;0;34mSeu alistamento será em {}.'.format(idade2))


