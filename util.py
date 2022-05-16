def cabecalho():
  print(f'\033[33m{"*"*31}\033[m')
  print(f'\033[37;41m{"JOGO DA VELHA V2.0":^31}\033[m')
  print(f'\033[33m{"*"*31}\033[m')
  print()
  
def tabuleiro(lista):
  
  linha = f'\033[34m{"+-----+-----+-----+":^31}\033[m'

  print(linha)
  print(f'      |  {lista[0]}  |  {lista[1]}  |  {lista[2]}  |')
  print(linha)
  print(f'      |  {lista[3]}  |  {lista[4]}  |  {lista[5]}  |')
  print(linha)
  print(f'      |  {lista[6]}  |  {lista[7]}  |  {lista[8]}  |')
  print(linha)

def validaInt(msg):
  while True:
    num = str(input(msg))
    if num not in '1,2,3,4,5,6,7,8,9':
      print('\033[35mERRO: Digite uma posição válida!\033[m')
    elif num == '':
      print('\033[35mERRO: Você não digitou uma posição!\033m')
    else:
      return num
      break

def checar(lista):
  # Ganhando na horizontal:
  if (lista[0] == lista[1] and lista[1] == lista[2]) or (lista[3] == lista[4] 
  and lista[4] == lista[5]) or (lista[6] == lista[7] and lista[7] == lista[8]): 
    return 'v'
    
  # Ganhando na vertical
  if (lista[0] == lista[3] and lista[3] == lista[6]) or (lista[1] == lista[4] 
  and lista[4] == lista[7]) or (lista[2] == lista[5] and lista[5] == lista[8]):
    return 'v'

  # Ganhando na diagonal:
  if (lista[0] == lista[4] and lista[4] == lista[8]) or (lista[2] == lista[4] 
  and lista[4] == lista[6]):
    return 'v'

  # Empatando:
  cont_vazio = 0
  for i in lista:
    if i not in '\033[32mX\033[m ,\033[31mO\033[m':
      cont_vazio += 1
  if cont_vazio == 0:
    return 'e'
  