import os
from util import cabecalho, tabuleiro, checar, validaInt

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

jogX = '\033[32mX\033[m'
jogO = '\033[31mO\033[m'
msgX = 'Vitória do \033[32mX\033[m !!!'
msgO = 'Vitória do \033[31mO\033[m !!!'
vitX = 0
vitO = 0
emp = 0

while True:

  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho()
    tabuleiro(lista)
    # Jogador X: 
    while True:
      n = validaInt('\n\033[37mQuer jogar\033[m \033[32m"X"\033[m \033[037mem qual posição? \033[m')
      if (lista[int(n)-1] == jogX) or (lista[int(n)-1] == jogO):
        print('\033[36mPosição ocupada!\033[m')
      else:
        lista[int(n)-1] = jogX
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho()
    tabuleiro(lista)
    ganhaX = checar(lista)
    if ganhaX == 'v':
      vitX += 1
      print(f'\n\033[36m{" FIM de JOGO ":-^31}\033[m')
      print(f'{msgX:^39}')
      print('\033[36m-\033[m'*31)
      break
    elif ganhaX == 'e':
      emp += 1
      print(f'\n\033[36m{" FIM de JOGO ":-^31}\033[m')
      print(f'{"EMPATE !!!":^35}')
      print('\033[35m-\033[m'*31)
      break
            
    # Jogador O:
    while True:
      n = validaInt('\n\033[37mQuer jogar\033[m \033[31m"0"\033[m \033[037mem qual posição? \033[m')
      if (lista[int(n)-1] == jogX) or (lista[int(n)-1] == jogO):
        print('\033[36mPosição ocupada!\033[m')
      else:
        lista[int(n)-1] = jogO
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho()
    tabuleiro(lista)
    ganhaO = checar(lista)
    if ganhaO == 'v':
      vitO += 1
      print(f'\n\033[36m{"FIM de JOGO.":-^31}\033[m')
      print(f'{msgO:^39}')
      print('\033[36m-\033[m'*31)
      break
    elif ganhaO == 'e':
      emp += 1
      print(f'\n\033[36m{" FIM de JOGO ":-^31}\033[m')
      print(f'{"EMPATE !!!":^35}')
      print('\033[36m-\033[m'*31)
      break
  
  while True:
    resp = str(input('\n\033[31mJogar outra vez?\033[m [S/N]: ')).strip()
    if resp not in 'SsNn':
      print('Digite uma opção válida')
    elif resp == '':
      print('Você não digitou uma opção')
    else:
      break

  if resp in 'Nn':
    break
  else:
    lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# PLacar:
print(f'\n\033[33m{"-":-^31}\033[m')
print(f'{"Placar:":^31}')
print(f'\033[33m{"-":-^31}\033[m')
print(f'Vitórias do X: {vitX}')
print(f'Vitórias do O: {vitO}')
print(f'Empates      : {emp}')
print(f'\033[33m{"-":-^31}\033[m')


print(f'\n\033[3;33m{"GAME OVER":^31}\033[m\n')