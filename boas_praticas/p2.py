dicionario = {}

def menu():
  print("1.Inserir Pessoa\n2.Listar pessoas cadastradas\n3.Buscar pessoa por CPF\n4.Buscar pessoa por telefone\n5.Remover pessoa por CPF\n6.Sair do Programa\n")

def existe_cpf(cpf):
  for key in dicionario.keys():
    if key == cpf:
      return 1
    else:
      return 0

def inserir_telefone():
  lista_tel = []
  print("Digite o telefone do aluno")
  tel = str(input(""))
  lista_tel.append(tel)
  chavetel = 1
  while(chavetel != 2):
    print("Deseja inserir mais algum telefone?\n1.Sim\n2.Não")
    chavetel = int(input(""))
    if(chavetel == 2):
      break
    novotel = str(input("Digite o novo telefone\n"))
    lista_tel.append(novotel)
  return lista_tel
  
def inserir_aluno():
  print("Digite o CPF do aluno")
  cpf = str(input(""))
  while (existe_cpf(cpf)):
    if existe_cpf(cpf) == 1:
      print("CPF já cadastrado, insira outro cpf")
    cpf = str(input(""))
  print("Digite o nome do aluno")
  nome = str(input(""))
  print("Digite o endereço do aluno")
  endereço = str(input(""))
  telefones = inserir_telefone()
  aluno = (cpf,nome,endereço,telefones)
  dicionario[aluno[0]] = (aluno[1], aluno[2], aluno[3])
  print("Aluno cadastrado\n")

def remover_aluno():
  print("Digite o CPF do aluno")
  cpf = str(input(""))
  for key in dicionario.keys():
    if key == cpf:
      dicionario.pop(key)
      return
  print("CPF não encontrado")
      
def procuraTelefone():
  print("Digite o telefone da pessoa")
  telefone_procurado = str(input(""))
  for chave,valor in dicionario.items():
    for telefone in valor[2]:
      if(telefone == telefone_procurado):
        return chave
  return 0

def procuraCpf():
  print("Digite o CPF da pessoa que você quer encontrar")
  procura = str(input(""))
  for key in dicionario.keys():
    if key == procura:
      return key
  return 0
  
print("Digite o valor correspondente a função desejada\n")
chave = -1
while(chave != 6):
  menu()
  chave = int(input(""))
  if(chave == 1):
    inserir_aluno()
  if(chave == 2):
    if(len(dicionario)==0):
      print("\nLista Vazia\n")
    else:
      for nome in dicionario.items():
        print(nome)
  if(chave==3):
    chave2 = procuraCpf()
    if chave2 == 0:
      print("Pessoa não encontrada")
    else:
      print(dicionario[chave2])
  if(chave == 4):
    chave3 = procuraTelefone()
    if(chave3 != 0):
      print(dicionario.get(chave3))
    else:
      print("Pessoa não encontrada")
  if(chave == 5):
    remover_aluno()
  if(chave == 6):
    print("Fim do programa!")